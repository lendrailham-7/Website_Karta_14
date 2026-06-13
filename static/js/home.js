const reveals = document.querySelectorAll(
    '.reveal'
);

function revealOnScroll() {

    reveals.forEach((element) => {

        const windowHeight = window.innerHeight;

        const elementTop = element.getBoundingClientRect().top;

        const visible = 100;

        if (elementTop < windowHeight - visible) {

            element.classList.add('active');

        }

    });

}

window.addEventListener(
    'scroll',
    revealOnScroll
);

revealOnScroll();
const previewImages = document.querySelectorAll(
    '.preview-image'
);

const modalImage = document.getElementById(
    'modalImage'
);

previewImages.forEach((image) => {

    image.addEventListener(
        'click',
        () => {

            console.log(
                'FOTO DIKLIK'
            );

            modalImage.src = image.src;

            const modal =
                new bootstrap.Modal(
                    document.getElementById(
                        'imageModal'
                    )
                );

            modal.show();

        }
    );

});