<p>
  Marvin Builds 是我的 YouTube 頻道，主題是真實的 AI agent 工作流程：我把實際的任務交給
  Claude Code、Codex 這些 agent，看它們怎麼讀需求、寫程式、跑測試、修錯誤、部署上線，
  然後把過程原封不動地錄下來。這一頁會自動與頻道同步，點縮圖就能直接在這裡播放。
</p>

<p>
  <a class="btn btn--danger" href="https://www.youtube.com/@MarvinBuildsAI?sub_confirmation=1" target="_blank" rel="noopener noreferrer">
    <i class="fab fa-youtube" aria-hidden="true"></i> 訂閱 Marvin Builds
  </a>
</p>

<div class="videos-section__head">
  <h2 id="latest-videos">最新影片</h2>
  <a class="videos-section__more" href="https://www.youtube.com/@MarvinBuildsAI/videos" target="_blank" rel="noopener noreferrer">更多影片 <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
</div>

{% if site.data.youtube.videos %}
{% include videos-strip.html items=site.data.youtube.videos %}
{% else %}
{% include youtube.html list="UULFh3pnlNkGStSGikqGJG64Qw" title="Marvin Builds 最新影片播放清單" %}
{% endif %}

<div class="videos-section__head">
  <h2 id="shorts">Shorts</h2>
  <a class="videos-section__more" href="https://www.youtube.com/@MarvinBuildsAI/shorts" target="_blank" rel="noopener noreferrer">更多 Shorts <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
</div>

{% if site.data.youtube.shorts %}
{% include videos-strip.html items=site.data.youtube.shorts shorts=true skip_script=site.data.youtube.videos %}
{% else %}
{% include youtube.html list="UUSHh3pnlNkGStSGikqGJG64Qw" shorts=true title="Marvin Builds Shorts 播放清單" %}
{% endif %}

{% include videos-jsonld.html %}
