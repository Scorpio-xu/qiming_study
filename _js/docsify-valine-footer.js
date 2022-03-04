"use strict";
window.$docsify = window.$docsify || {}, window.$docsify.plugins = [function (n, i) {
  n.ready((function () {
    window.Valine || console.warn(
      "please include `<script src='//unpkg.com/valine/dist/Valine.min.js'><\/script>` before init $docsify"
    )
  }));
  n.mounted((function () {
    var n = Docsify.dom,
      i = n.create("div");
    i.id = "vcomments";
    i.style = "max-width: 90% !important; margin: 0 auto 20px;";
    n.appendTo(n.find(".content"), i);
    const currentYear = new Date().getFullYear();
    var footer = n.create("footer");
    footer.className = "markdown-section";
    footer.innerHTML = `<hr/>
        <span id="busuanzi_container_page_pv" style='display:none'>
          🐱本站阅读量：<span id="busuanzi_value_page_pv"></span>次
        </span></br></br>
        <span>本站内容采用<a href = "https://creativecommons.org/licenses/by-nc-sa/4.0/">
        <i class="fab fa-creative-commons"></i> BY-NC-SA 4.0</a>许可协议，支持转载，请勿用于商业用途。</br></br>
        Copyright © 2021-${currentYear} <a href="https://qiming.info" target="_blank">QIMING.INFO</a>. All Rights Reserved.`
    n.appendTo(n.find(".content"), footer)
  }));
  n.doneEach((function () {
    i.config.Valine = i.config.Valine || {};
    var n = Object.assign({
      el: "#vcomments",
      path: "full" === i.config.Valine.docPath ? location.pathname + location.hash.replace(/\?.+/,
        "") : location.hash.replace(/\?.+/, "")
    }, i.config.Valine);
    n.appId && n.appKey ? new Valine(n) : console.warn("sorry , appId and appKey must be required .")
  }))
}].concat(window.$docsify.plugins || []);