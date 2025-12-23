document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const statusMessage = document.getElementById('status-message');
    const resultsDiv = document.getElementById('results');
    const originalImage = document.getElementById('original-image');
    const annotatedImage = document.getElementById('annotated-image');
    const countDisplay = document.getElementById('count');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const file = fileInput.files[0];
        if (!file) {
            statusMessage.textContent = 'Please select a file to upload.';
            statusMessage.classList.remove('hidden');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        statusMessage.textContent = 'Analyzing image...';
        statusMessage.classList.remove('hidden');
        resultsDiv.classList.add('hidden');

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Something went wrong.');
            }

            const data = await response.json();
            
            // Display images and count
            originalImage.src = URL.createObjectURL(file);
            annotatedImage.src = data.summary.annotated_url;
            countDisplay.textContent = data.summary.count;
            
            statusMessage.classList.add('hidden');
            resultsDiv.classList.remove('hidden');

        } catch (error) {
            console.error('Error:', error);
            statusMessage.textContent = `Error: ${error.message}`;
            statusMessage.classList.remove('hidden');
        }
    });
});
