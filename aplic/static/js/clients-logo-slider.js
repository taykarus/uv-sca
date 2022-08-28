//====== Clients Logo Slider
tns({
    container: '.client-logo-carousel',
    slideBy: 'page',
    autoplay: true,
    autoplayButtonOutput: false,
    mouseDrag: true,
    gutter: 15,
    nav: false,
    controls: false,
    responsive: {
        0: {
            items: 1,
        },
        540: {
            items: 3,
        },
        768: {
            items: 4,
        },
        992: {
            items: 4,
        },
        1170: {
            items: 6,
        }
    }
});