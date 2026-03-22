document.addEventListener('DOMContentLoaded', function() {
    setupUploadPreview();
});

function setupUploadPreview() {
    const form = document.getElementById('uploadForm');
    if (!form) return;

    const imageInput = form.querySelector('input[type="file"]');
    const titleInput = form.querySelector('input[name="title"]');
    const captionInput = form.querySelector('textarea[name="caption"]');

    const previewImage = document.getElementById('previewImage');
    const previewTitle = document.getElementById('previewTitle');
    const previewCaption = document.getElementById('previewCaption');

    // Image preview
    if (imageInput) {
        imageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    previewImage.innerHTML = `<img src="${event.target.result}" alt="Preview">`;
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Title preview
    if (titleInput) {
        titleInput.addEventListener('input', function() {
            const text = this.value.trim() || "Pet's Name";
            previewTitle.textContent = text;
        });
    }

    // Caption preview
    if (captionInput) {
        captionInput.addEventListener('input', function() {
            const text = this.value.trim() || "Your memory will appear here...";
            previewCaption.textContent = text;
        });
    }
}
