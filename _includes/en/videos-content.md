<p>
  Marvin Builds is my YouTube channel about real AI-agent workflows: I hand actual tasks to agents
  like Claude Code and Codex, then record — unedited — how they read requirements, write code, run
  tests, fix mistakes, and deploy. This page stays in sync with the channel automatically, and every
  thumbnail plays right here.
</p>

<p>
  <a class="btn btn--danger" href="https://www.youtube.com/@MarvinBuildsAI?sub_confirmation=1" target="_blank" rel="noopener noreferrer">
    <i class="fab fa-youtube" aria-hidden="true"></i> Subscribe to Marvin Builds
  </a>
</p>

<div class="videos-section__head">
  <h2 id="latest-videos">Latest videos</h2>
  <a class="videos-section__more" href="https://www.youtube.com/@MarvinBuildsAI/videos" target="_blank" rel="noopener noreferrer">More videos <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
</div>

{% if site.data.youtube.videos %}
{% include videos-strip.html items=site.data.youtube.videos play_label="Play: " %}
{% else %}
{% include youtube.html list="UULFh3pnlNkGStSGikqGJG64Qw" title="Marvin Builds latest videos playlist" %}
{% endif %}

<div class="videos-section__head">
  <h2 id="shorts">Shorts</h2>
  <a class="videos-section__more" href="https://www.youtube.com/@MarvinBuildsAI/shorts" target="_blank" rel="noopener noreferrer">More Shorts <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
</div>

{% if site.data.youtube.shorts %}
{% include videos-strip.html items=site.data.youtube.shorts shorts=true skip_script=site.data.youtube.videos play_label="Play: " %}
{% else %}
{% include youtube.html list="UUSHh3pnlNkGStSGikqGJG64Qw" shorts=true title="Marvin Builds Shorts playlist" %}
{% endif %}

{% include videos-jsonld.html %}
