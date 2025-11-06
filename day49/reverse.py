<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>AgriSense.AI — Interactive Flowchart</title>
  <style>
    :root{
      --bg: #f6f8fb;
      --card: #ffffff;
      --accent1: linear-gradient(135deg,#1fa2ff 0%, #12d8fa 100%);
      --accent2: linear-gradient(135deg,#7afcff 0%, #b692ff 100%);
      --accent3: linear-gradient(135deg,#7be495 0%, #2bb673 100%);zz
      --muted: #6b7280;
      --glass: rgba(255,255,255,0.7);
      --shadow: 0 10px 30px rgba(16,24,40,0.08);
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%; margin:0; background:var(--bg); color:#0f172a;}
    .container{max-width:1150px; margin:28px auto; padding:20px;}
    header{display:flex; gap:16px; align-items:center; margin-bottom:18px}
    header h1{font-size:20px; margin:0}
    .controls{margin-left:auto; display:flex; gap:8px; align-items:center}
    .card{background:var(--card); border-radius:14px; padding:18px; box-shadow:var(--shadow)}
    .flow-wrap{display:flex; align-items:center; justify-content:space-between; gap:12px; padding:28px; margin:18px 0}
    .node{
      min-width:180px; max-width:220px; padding:18px; border-radius:12px;
      color:white; text-align:center; box-shadow:0 6px 18px rgba(12,18,36,0.08);
      cursor:pointer; position:relative;
      transition:transform .18s ease, box-shadow .18s ease;
    }
    .node:hover{transform:translateY(-6px); box-shadow:0 18px 40px rgba(12,18,36,0.12)}
    .node h3{margin:6px 0 4px 0; font-size:18px}
    .node p{margin:0; font-size:13px; opacity:0.95}
    .node .icon{height:48px; display:flex; align-items:center; justify-content:center; font-size:24px}
    .connector{flex:1; height:4px; background:linear-gradient(90deg,#e6edf9, #f1f6ff); border-radius:999px; position:relative}
    .arrow{position:absolute; right:-10px; top:-8px; width:24px; height:24px; transform:rotate(0deg)}
    .subtitle{font-size:13px; color:var(--muted); margin-top:6px}
    .panel{margin-top:12px; display:flex; gap:12px; align-items:flex-start}
    .panel .left{flex:1}
    .panel .right{width:380px}
    .meta{display:flex; gap:8px; flex-wrap:wrap}
    .chip{background:rgba(255,255,255,0.7); padding:6px 10px; border-radius:10px; font-size:13px; border:1px solid rgba(15,23,42,0.04)}
    .controls .btn{background:#0f172a;color:white;padding:8px 12px;border-radius:8px;border:none;cursor:pointer}
    .controls .btn.secondary{background:transparent;color:var(--muted);border:1px solid rgba(15,23,42,0.06)}
    .details{padding:12px; border-radius:10px; background:linear-gradient(180deg, rgba(255,255,255,0.9), rgba(250,250,255,0.9)); border:1px solid rgba(15,23,42,0.04)}
    .small{font-size:13px;color:var(--muted)}
    /* color mini-map */
    .swatches{display:flex; gap:8px; margin-top:8px}
    .swatch{width:38px;height:38px;border-radius:8px;box-shadow:0 6px 20px rgba(12,18,36,0.06);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700}
    /* AI prompt box */
    .prompt{background:#0b1220;color:#fff;padding:12px;border-radius:8px;font-family:monospace;font-size:13px}
    /* version compare */
    .version-toggle{display:flex; align-items:center; gap:8px}
    input[type=range]{width:160px}
    /* responsive */
    @media (max-width:980px){
      .flow-wrap{flex-direction:column; gap:18px}
      .panel .right{width:100%}
    }
  </style>
  <!-- html2canvas for export -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <h1>AgriSense.AI — Farm → Data Capture → Analysis → Insights → Production</h1>
        <div class="small">Interactive flowchart — integrates smart features for FMCG supply chain alignment</div>
      </div>

      <div class="controls">
        <div style="display:flex; gap:8px; align-items:center;">
          <label class="small">Skill:</label>
          <select id="skillSelect" class="chip">
            <option value="beginner">Beginner</option>
            <option value="intermediate" selected>Intermediate</option>
            <option value="expert">Expert</option>
          </select>
        </div>

        <div style="display:flex; gap:8px; align-items:center;">
          <label class="small">Version:</label>
          <div class="version-toggle chip">
            <input type="radio" name="ver" id="v1" value="v1" checked> <label for="v1">v1</label>
            &nbsp;
            <input type="radio" name="ver" id="v2" value="v2"> <label for="v2">v2</label>
          </div>
        </div>

        <button class="btn" id="exportBtn">Export PNG</button>
        <button class="btn secondary" id="resetBtn">Reset Highlights</button>
      </div>
    </header>

    <div class="card">
      <div class="flow-wrap" id="flowRoot">
        <!-- Farm node -->
        <div class="node" id="node-farm" data-key="farm" style="background:var(--accent3);">
          <div class="icon">🚜</div>
          <h3>Farm</h3>
          <p class="subtitle">Sensors & field teams</p>
        </div>

        <!-- connector -->
        <div class="connector" aria-hidden><svg class="arrow" viewBox="0 0 24 24"><path d="M3 12h14l-4 4" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>

        <!-- Data Capture / IoT node -->
        <div class="node" id="node-capture" data-key="capture" style="background:var(--accent1);">
          <div class="icon">📡</div>
          <h3>Data Capture</h3>
          <p class="subtitle">IoT sensors, drones, mobile apps</p>
        </div>

        <div class="connector" aria-hidden><svg class="arrow" viewBox="0 0 24 24"><path d="M3 12h14l-4 4" fill="none" stroke="#06b6d4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>

        <!-- AgriSense.AI / Analysis -->
        <div class="node" id="node-analysis" data-key="analysis" style="background:var(--accent2); color:#051226;">
          <div class="icon">☁️</div>
          <h3>AgriSense.AI</h3>
          <p class="subtitle">Cloud analytics, ML models</p>
        </div>

        <div class="connector" aria-hidden><svg class="arrow" viewBox="0 0 24 24"><path d="M3 12h14l-4 4" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>

        <!-- Production -->
        <div class="node" id="node-prod" data-key="production" style="background:linear-gradient(135deg,#ffb86b,#ff8b8b); color:#102331;">
          <div class="icon">🏭</div>
          <h3>Production</h3>
          <p class="subtitle">FMCG procurement & manufacturing</p>
        </div>
      </div>

      <!-- Details panel (left: node info, right: insights, palette, tools) -->
      <div class="panel">
        <div class="left">
          <div class="details card" id="detailsBox">
            <h3 id="d-title">Click a node to view details</h3>
            <div id="d-desc" class="small">Nodes explain their function, recommended tools, and AI suggestions.</div>

            <div style="margin-top:12px;">
              <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">
                <div class="chip">Impact</div>
                <div class="chip">Sustainability</div>
                <div class="chip">Traceability</div>
              </div>

              <div id="d-tools" style="margin-top:8px;">
                <strong>Recommended tools:</strong>
                <div class="meta" id="toolsMeta" style="margin-top:8px">
                  <!-- injected -->
                </div>
              </div>

              <div id="d-metrics" style="margin-top:12px;">
                <strong>Sample Metrics:</strong>
                <div style="margin-top:8px" id="metricsList" class="small">
                  <!-- injected -->
                </div>
              </div>

              <div style="margin-top:10px;">
                <strong>AI Step Recommender</strong>
                <div class="small" id="aiRecommender" style="margin-top:6px">Choose a node + skill level to get a suggested next step.</div>
              </div>
            </div>
          </div>

          <!-- color mini-map -->
          <div style="margin-top:14px;" class="card details">
            <strong>Color Palette Suggestions</strong>
            <div class="swatches" id="swatches">
              <div class="swatch" style="background:linear-gradient(135deg,#1fa2ff,#12d8fa)">A</div>
              <div class="swatch" style="background:linear-gradient(135deg,#7afcff,#b692ff)">B</div>
              <div class="swatch" style="background:linear-gradient(135deg,#7be495,#2bb673)">C</div>
              <div class="swatch" style="background:linear-gradient(135deg,#ffb86b,#ff8b8b)">D</div>
            </div>
            <div class="small" style="margin-top:10px">Use Palette C for "agriculture" branding; Palette B for analytics dashboards; Palette D for production/warning states.</div>
          </div>
        </div>

        <div class="right">
          <div class="card details">
            <strong>AI  Tips (quick)</strong>
            <div class="prompt" id="promptBox">
#  "Isometric smart farm with sensors and cloud analytics, modern blue/green palette, photorealistic"
# StableDiffusion: "agritech dashboard UI, data visualizations, farmers interacting with tablets, clean design"
# Analysis prompt: "Given sensor dataset [soil_moisture,temp,ndvi], predict weekly yield and irrigation schedule"
            </div>

            <div style="margin-top:12px;">
              <strong>Version Comparison</strong>
              <div class="small" style="margin-top:6px">Toggle Version to compare feature set:</div>
              <ul id="versionList" class="small" style="margin-top:8px">
                <!-- injected -->
              </ul>
            </div>

            <div style="margin-top:12px;">
              <strong>Export / Deliverables</strong>
              <div class="small" style="margin-top:6px">
                • Slide-ready PNG export (use Export PNG).<br>
                • Exported metrics & CSV (demo) — integrate with procurement ERPs via API.<br>
                • Suggest adding pilot results (3 farms x 2 months) in appendix.
              </div>
            </div>

            <div style="margin-top:12px;">
              <strong>Admin Actions</strong>
              <div style="margin-top:8px; display:flex; gap:8px;">
                <button class="btn" id="suggestBtn">Get AI Suggestion</button>
                <button class="btn secondary" id="downloadCSV">Download CSV (demo)</button>
              </div>
            </div>

          </div>
