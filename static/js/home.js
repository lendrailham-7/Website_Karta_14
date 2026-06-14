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
document.addEventListener('DOMContentLoaded', () => {

    const typingDescription = document.getElementById('typing-description');

    if (!typingDescription) return;

    const text = "Pemuda Berkarya, Masyarakat Sejahtera.\nBersama membangun lingkungan yang aktif, kreatif, dan peduli sosial.";

    let index = 0;

    function typeDescription() {
        if (index < text.length) {
            const char = text.charAt(index);

            typingDescription.innerHTML += char === '\n' ? '<br>' : char;

            index++;
            setTimeout(typeDescription, 25);
        }
    }

    typeDescription();

});