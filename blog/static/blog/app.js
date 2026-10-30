(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector(".theme-toggle");
  const themeColor = document.querySelector('meta[name="theme-color"]');

  const updateThemeUI = () => {
    if (!themeButton) return;

    const isDark = root.dataset.theme === "dark";
    themeButton.setAttribute("aria-label", isDark ? "切换浅色模式" : "切换深色模式");
    themeButton.setAttribute("aria-pressed", String(isDark));
    if (themeColor) {
      themeColor.setAttribute("content", isDark ? "#10161b" : "#f3eee5");
    }
  };

  updateThemeUI();

  themeButton?.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = nextTheme;
    try {
      localStorage.setItem("blog-theme", nextTheme);
    } catch {
      // Theme switching still works when storage is unavailable.
    }
    updateThemeUI();
  });

  const copyButton = document.querySelector("[data-copy-url]");
  copyButton?.addEventListener("click", async () => {
    const label = copyButton.querySelector("span");
    const originalLabel = label?.textContent || "复制链接";
    const url = copyButton.dataset.copyUrl;

    try {
      await navigator.clipboard.writeText(url);
    } catch {
      const textarea = document.createElement("textarea");
      textarea.value = url;
      textarea.setAttribute("readonly", "");
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      textarea.remove();
    }

    if (label) {
      label.textContent = "已复制";
      window.setTimeout(() => {
        label.textContent = originalLabel;
      }, 1800);
    }
  });

  const progressBar = document.querySelector("[data-reading-progress]");
  const article = document.querySelector(".article-page");

  if (progressBar && article && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    let ticking = false;

    const updateProgress = () => {
      const articleTop = article.offsetTop;
      const articleHeight = article.offsetHeight;
      const visibleEnd = window.scrollY + window.innerHeight;
      const rawProgress = (visibleEnd - articleTop) / articleHeight;
      const progress = Math.min(1, Math.max(0, rawProgress));
      progressBar.style.transform = `scaleX(${progress})`;
      ticking = false;
    };

    const requestProgressUpdate = () => {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(updateProgress);
    };

    updateProgress();
    window.addEventListener("scroll", requestProgressUpdate, { passive: true });
    window.addEventListener("resize", requestProgressUpdate, { passive: true });
  }
})();
