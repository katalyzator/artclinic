$(function () {
    var worksSlider = $('.works-slider');

    $(".uk-navbar-nav > li > a").on("click", function () {
        $(".uk-navbar-nav > li").removeClass("uk-active");
        $(this).parent("li").addClass("uk-active");
    });

    $('.uk-navbar-nav a[href^="#"], .all-services-link, .uk-logo').on("click", function (t) {
        var e = $(this.getAttribute("href"));
        e.length && (t.preventDefault(), $("html, body").stop().animate({scrollTop: e.offset().top}, 1e3));
    });

    worksSlider.slick({
        infinite: false,
        dots: true,
        lazyLoad: 'ondemand',
        slidesToShow: 1,
        slidesToScroll: 1,
        speed: 500,
        fade: true,
        cssEase: 'ease-in',
        prevArrow: '<a href="#" class="uk-position-bottom-left" uk-slidenav-previous></a>',
        nextArrow: '<a href="#" class="uk-position-bottom-right" uk-slidenav-next></a>',
        draggable: false,
    });

    $('.double-image').twentytwenty({
        before_label: 'До', // Set a custom before label
        after_label: 'После', // Set a custom after label
    });

    worksSlider.on('click', '.uk-slidenav, .slick-dots li', function () {
        var currentSlider = $('.works-slider .slick-list .slick-active');
        var sliderIndex = currentSlider.attr('data-slick-index');

        $('.work-type li').each(function () {
            var typeIndex = $(this).attr('data-type');

            if (sliderIndex === typeIndex) {
                $('.work-type li').removeClass('active-type');
                $(this).addClass('active-type');
            }

        })
    });

    $('.service_shower').each(function (i, obj) {
        $(obj).on('click', function (event) {
            event.preventDefault();
            var that = this;
            var url = $(that).attr('data-ajax-url'); // the script where you handle the form input.
            $.ajax({
                method: "GET",
                dataType: "HTML",
                url: url,
                success: function (response) {
                    $('#modal-center').html(response);
                    UIkit.modal("#modal-center").show();
                }
            });
            // avoid to execute the actual submit of the form.
        });
    });

    $('.specialist-shower').each(function (i, obj) {
        $(obj).on('click', function (event) {
            event.preventDefault();
            var that = this;
            var url = $(that).attr('href'); // the script where you handle the form input.
            $.ajax({
                method: "GET",
                dataType: "HTML",
                url: url,
                success: function (response) {
                    $('#employer-modal').html(response);
                    UIkit.modal("#employer-modal").show();
                }
            });
            // avoid to execute the actual submit of the form.
        });
    });

    $('.application-form').submit(function (event) {
        event.preventDefault();
        var url = $('.application-form').attr('action');
        $.ajax({
            method: "POST",
            dataType: "HTML",
            data: $('.application-form').serialize(),
            url: url,
            success: function (response) {
                document.getElementsByClassName('application-form')[0].reset();
                UIkit.modal("#appointment-modal").hide();
                alert('Заявка успешно отправлена');
            }
        });
    });

    $('.email-form').submit(function (event) {
        event.preventDefault();
        var url = $('.email-form').attr('action');
        $.ajax({
            method: "POST",
            dataType: "HTML",
            data: $('.email-form').serialize(),
            url: url,
            success: function (response) {
                document.getElementsByClassName('email-form')[0].reset();
                alert('Вы успешно подписались на наши рассылки');
            }
        });
    });
});