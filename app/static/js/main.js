// Simple client-side hook
document.addEventListener('DOMContentLoaded', () => {
  const footer = document.querySelector('footer small');
  if (footer) {
    const now = new Date();
    footer.insertAdjacentText('beforeend', ` · ${now.toLocaleString()}`);
  }
});

