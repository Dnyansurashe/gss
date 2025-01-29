<script>
    document.querySelector('.comment-form').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const username = e.target.username.value.trim();
        const comment = e.target.comment.value.trim();

        if (username && comment) {
            // Display comment in the comment section
            const commentSection = document.querySelector('.comments-display');
            const newComment = document.createElement('div');
            newComment.classList.add('comment');
            newComment.innerHTML = `<p><strong>${username}:</strong> ${comment}</p>`;
            commentSection.appendChild(newComment);

            // Optionally, save to localStorage for persistence
            const savedComments = JSON.parse(localStorage.getItem('comments')) || [];
            savedComments.push({ username, comment });
            localStorage.setItem('comments', JSON.stringify(savedComments));

            // Clear the form fields
            e.target.username.value = '';
            e.target.comment.value = '';
        }
    });

    // Load saved comments from localStorage
    window.addEventListener('DOMContentLoaded', () => {
        const savedComments = JSON.parse(localStorage.getItem('comments')) || [];
        const commentSection = document.querySelector('.comments-display');
        
        savedComments.forEach(({ username, comment }) => {
            const commentDiv = document.createElement('div');
            commentDiv.classList.add('comment');
            commentDiv.innerHTML = `<p><strong>${username}:</strong> ${comment}</p>`;
            commentSection.appendChild(commentDiv);
        });
    });
</script>
