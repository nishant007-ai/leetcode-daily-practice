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
          <label class="sm