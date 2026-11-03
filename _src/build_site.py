"""Generates the site pages (index.html and projects/*.html) in the repository root.

Run from anywhere:  python3 _src/build_site.py
Images live in img/, styles in style.css; this script only writes HTML."""
import os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(ROOT)
SVG = lambda n: open(f'{ROOT}/svg/{n}.svg').read()

EMAIL = 'laraquiilyes@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/ilyes-laraqui-houssa%C3%AFni-b3003a238'
PDF = 'Ilyes_Laraqui_Houssaini_Portfolio.pdf'

TAGS = [('design', 'Design'), ('data', 'Data & analysis'), ('modelling', 'Modelling & simulation'), ('quant', 'Quantitative')]
TAGNAME = dict(TAGS)


def fig(src, cap, cls='', alt=None, contain=False):
    c = ' class="contain"' if contain else ''
    return f'<figure class="{cls}"><div class="frame"><img src="../img/{src}" alt="{html.escape(alt or cap)}" loading="lazy"{c}></div><figcaption>{cap}</figcaption></figure>'


def svgfig(name, cap, cls='', note=None):
    n = f'<span class="note">{note}</span>' if note else ''
    return f'<figure class="svg {cls}"><div class="frame">{SVG(name)}</div><figcaption>{cap}{n}</figcaption></figure>'


def nums(items):
    return '<dl class="nums">' + ''.join(f'<div><dt>{v}</dt><dd>{l}</dd></div>' for v, l in items) + '</dl>'


PROJECTS = [
 dict(slug='racing-bulls-wind-tunnel', title='Wind tunnel hardware at Racing Bulls F1',
      card='Model parts and test rigs for the aero team: a full wheel assembly with tyre deformers, a radiator correlation rig, and fixes that kept the tunnel running.',
      tags=['design', 'modelling'], stat=('0.8 mm', 'FEA vs laser scan'),
      thumb=('svg', 'deformer'),
      role='Mechanical design placement, Wind Tunnel Engineering', where='Racing Bulls F1 (Visa Cash App RB)', when='Jul 2025 – Jul 2026',
      tools='Siemens NX, NX FEA, BS 8888 GD&T',
      lead='A year designing the hardware the aero team uses to test new ideas in the wind tunnel, from model parts to test rigs, and following each part through manufacture, assembly and testing.',
      nums=[('0.8 mm', 'max tyre-shape difference, FEA vs laser scan'), ('6 m', 'radiator rig, 14 bonded sections'), ('15 / 15', 'assemblies correct after a 5-year problem was fixed'), ('3 h', 'from part clash found to new drawing issued')],
      body=lambda: f'''
<section class="two">
 <div>
  <h2>Wheel assembly and tyre deformers</h2>
  <p>Tyre shape has a big effect on diffuser and rear brake duct flow, so the tyre in the tunnel has to match the shape it has on track. Starting from the aero surfaces, I designed the rims, hubs, wheel covers and the deformers that push the outboard shoulder of the tyre out to its loaded shape. I used one representative profile and revolved it through 360°.</p>
  <p>I owned the parts end-to-end: released them to manufacturing, assembled and balanced the rims, and fitted the wheels to the model myself. The built assembly matched the FEA model to within <b>0.8 mm</b> on a laser scan.</p>
 </div>
 {svgfig('deformer', 'Section through the wheel. My own simplified illustration, not the actual part.', 'diagram')}
</section>
<section class="two">
 <div>
  <h2>Radiator correlation rig</h2>
  <p>Model radiators are tested on a rig and correlated with CFD before they go on the tunnel model. I designed a full-size version of that rig concept: a 6 m "mini wind tunnel" built from 14 bonded and sanded sections, with a real radiator core mounted inside it as a cross-section.</p>
  <p>It measures the pressure and velocity loss across the core, so the model radiator can be correlated against the real one.</p>
 </div>
 {svgfig('radiator', 'Rig layout. My own simplified illustration, not the actual rig.', 'diagram')}
</section>
<section class="three">
 <div><h3>A 5-year assembly problem, fixed</h3><p>One model assembly had been unreliable for more than five years. I traced it to clearances tighter than 0.010 mm that no drawing captured, added the correct GD&amp;T annotation, and checked the fix over 15 assembly iterations. All 15 assembled correctly.</p></div>
 <div><h3>Overnight fix for a part clash</h3><p>At 20:00 I was the last mechanical engineer on site when the Model Shop found a part clash that had to be fixed before a 06:00 tunnel run. I up-issued the part, issued the new drawing within 3 hours, and stayed until it was made and fitted to the model for checking. The aero component it carried was then tested and released quickly as a track upgrade.</p></div>
 <div><h3>Rigs, model parts and race weekends</h3><p>I designed several rigs for testing new technologies for the model, including a calibration rig and bench-test rigs, plus suspension pick-up parts checked against kinematic points. I also improved the model's metrology datum system. On race weekends I supported the race engineering team in the ops room by monitoring competitor radio.</p></div>
</section>
<p class="nda">Racing Bulls work is covered by an NDA, so no company images are shown. The diagrams are my own.</p>
'''),

 dict(slug='fx-central-bank-drift', title='Do FX pairs drift before central bank decisions?',
      card='An event study on 185 Fed, ECB and BoE meetings with a permutation test and a walk-forward backtest. The answer was no, and the work shows how I made sure of it.',
      tags=['quant', 'data'], stat=('p = 0.97', 'no drift found'),
      thumb=('svg', 'fx-equity'),
      role='Capstone project, Data Structures & Algorithms', where='MSc Financial Engineering, Imperial College London', when='Oct 2026',
      tools='Python (pandas, NumPy), yfinance, matplotlib',
      lead='US equities are known to drift up before Fed announcements. I tested whether EUR/USD, GBP/USD and USD/JPY do something similar the day before the Fed, ECB and Bank of England announce rate decisions.',
      nums=[('185', 'scheduled meetings, 2019–2026'), ('p = 0.97', 'pooled permutation test, 20,000 shuffles'), ('−1.06', 'Sharpe of the walk-forward strategy'), ('161', 'trades, each out-of-sample by construction')],
      body=lambda: f'''
<section class="two">
 <div>
  <h2>Set-up</h2>
  <p>For each meeting I measured the return over the one full trading day before the decision, stopping short of decision day so the market's reaction to the announcement isn't mixed in. ECB and BoE meetings use EUR/USD and GBP/USD. Fed meetings use a dollar-strength index built from all three pairs.</p>
  <p>The control group is every ordinary trading day, excluding any day within 3 days of another bank's meeting: 4,083 observations. Unscheduled emergency cuts, like March 2020, were left out because the market couldn't have known they were coming.</p>
  <h2>Testing for an effect</h2>
  <p>FX returns have fat tails, so instead of a t-test I used a permutation test: shuffle the event and control labels 20,000 times and see how often chance alone produces a difference as large as the real one. Pooled p = 0.97, and no bank on its own came close to significance. Splitting the sample in time, the effect also flips sign: +1.97 bps in 2019–2023, −3.89 bps in 2024–2026.</p>
 </div>
 <div class="stack">
  {fig('fx-null.png', 'The observed difference (−0.12 bps) sits in the middle of 20,000 random relabellings.', contain=True)}
  {fig('fx-by-bank.png', 'Pre-announcement return vs an ordinary day, by bank, with p-values.', contain=True)}
 </div>
</section>
<section class="two">
 <div>
  <h2>Trying to trade it anyway</h2>
  <p>Before each meeting, the strategy trades in the direction of that bank's average return at its previous meetings, with a minimum of 8 meetings of history and 1.5 bps cost each way. The <code>.shift(1)</code> in the signal makes sure a meeting's own outcome never feeds its own trade, so every one of the 161 trades is out-of-sample.</p>
  <p>It lost money in every cut of the data: net −14.2%, Sharpe −1.06, maximum drawdown −15.2%. Returns were negative even before costs.</p>
  <h2>What I'd want a reviewer to notice</h2>
  <ul>
   <li>Every setting (window, control buffer, minimum history) was fixed before I looked at results. Nothing was swept to find the best-looking value.</li>
   <li>When the backtest lost money, I didn't flip the sign of the rule. That would have been fitting to the result.</li>
   <li>The three pairs aren't three independent bets: the dollar is in all of them, so the strategy is closer to one dollar view than a diversified one.</li>
  </ul>
 </div>
 {svgfig('fx-equity', 'Walk-forward strategy, net of costs, rebuilt from the trade log.', 'chart')}
</section>
'''),

 dict(slug='front-suspension', title='Pull-rod mono-shock front suspension',
      card='My dissertation for the UCL Formula Student car: one damper for both wheels, flexures instead of bearings, and a prototype to check the kinematics.',
      tags=['design', 'modelling'], stat=('−26%', 'system mass'),
      thumb=('img', 'front-corner.jpg'),
      role='Individual dissertation (77/100), as Technical Director', where='UCL Formula Student', when='2024 – 2025',
      tools='Fusion 360, MATLAB, kinematic simulation, hand calculations',
      lead="UCL's front suspension hadn't changed since 2014: push-rod double wishbones with a damper at each corner. It was heavy and expensive, and drivers said the car lacked grip in fast corners.",
      nums=[('−26.2%', 'system mass, 7.73 → 5.70 kg (target −10%)'), ('−9.2%', 'system cost, £6,724 → £6,108'), ('0.22°', 'max camber difference, prototype vs simulation'), ('6 / 6', 'design targets met')],
      body=lambda: f'''
<section class="two">
 <div>
  <h2>Geometry from what the tyre needs</h2>
  <p>I doubled the camber-gain target to −0.8° per inch of travel (from −0.4°), set the pick-up points from the swing-axle length (1819 mm) and checked them in kinematic simulation: camber gain −0.78°/in, motion ratio 1.42 and constant in bump, roll centre 42 mm, anti-dive 11%, bump steer 0.05 mm/in.</p>
  <h2>One damper, tunable roll</h2>
  <p>A single damper handles both wheels, which lowers the centre of mass. The shared rocker works as a torsion bar in roll, so roll stiffness can be changed separately from heave by choosing one of three pull-rod mounting holes.</p>
  <h2>Sized for the worst case</h2>
  <p>I hand-calculated braking, acceleration, cornering and a 5 g kerb-strike load case, giving member loads up to 11.7 kN, and chose T45 wishbones, 4130 tie rods and EN24T steel. I replaced spherical bearings with blade flexures, sized in a MATLAB script using large-deflection beam theory and checked for bending, von Mises and buckling.</p>
 </div>
 <div class="stack">
  {fig('front-corner.jpg', 'Pull-rod front corner, re-using the existing uprights.')}
  {fig('rocker.jpg', 'One damper for both wheels. The rocker doubles as an adjustable torsion bar.', 'wide')}
 </div>
</section>
<section class="two">
 <div>
  <h2>Checked on a real prototype</h2>
  <p>I built a plywood and 3D-printed rig to measure the kinematics. Measured camber gain matched the simulation to within 0.22° across the full wheel travel.</p>
  <div class="pair">{fig('prototype.jpg', 'Kinematic prototype I built.')}{fig('flexures.jpg', 'Blade flexures on the car.')}</div>
 </div>
 <div class="stack">
  {svgfig('camber', 'Camber change vs wheel travel: simulation vs prototype.', 'chart')}
  {svgfig('mass', 'Mass by assembly (g): previous design in grey, mine in pink.', 'chart')}
 </div>
</section>
'''),

 dict(slug='telemetry-driver-coaching', title='Telemetry maps and driver coaching',
      card='MATLAB tools that turn logged car data into track heat maps, used to compare setups and coach drivers.',
      tags=['data'], stat=('5.8 s', 'lap time gained'),
      thumb=('img', 'throttle-updated.png'),
      role='Performance Leader', where='UCL Formula Student', when='2023 – 2024',
      tools='MATLAB, LifeRacing ECU data',
      lead='I wanted drivers and engineers to see where on the track time was being won and lost, rather than reading it off a column of numbers.',
      nums=[('5.8 s', 'lap time gained by the slower driver'), ('1:10.623 → 1:04.832', 'lap time before and after coaching')],
      body=lambda: f'''
<section class="two">
 <div>
  <p>I wrote MATLAB scripts that turn logged throttle, brake, gear, ride height and roll and yaw rates into heat maps drawn on the track outline. I first checked the tool on FS Sim Series data, comparing a generic setup with an updated one. The maps here are from that check.</p>
  <p>I then ran the same tool on the car's LifeRacing ECU data. Overlaying two drivers showed where the slower one was losing time and where to brake and change up. Their lap came down from <b>1:10.623 to 1:04.832</b>.</p>
 </div>
 <div class="pair">{fig('throttle-generic.png', 'Throttle map, generic setup.', contain=True)}{fig('throttle-updated.png', 'Throttle map, updated setup.', contain=True)}</div>
</section>
'''),

 dict(slug='cooling-model', title='Cooling model and sidepod redesign',
      card='A Simscape model that found why the car overheated, leading to a sidepod redesign that brought coolant down from 120 °C to 85 °C.',
      tags=['modelling', 'data'], stat=('120 → 85 °C', 'peak coolant'),
      thumb=('img', 'fs-car.jpg'),
      role='Performance Leader', where='UCL Formula Student', when='2023 – 2024',
      tools='MATLAB, Simulink / Simscape Thermal Liquid',
      lead='The car overheated in endurance: coolant passed 100 °C after five laps and peaked at 120 °C, and the fans had to run all the time.',
      nums=[('30%', 'of the radiator core getting useful airflow'), ('85 °C', 'coolant after the redesign, at 20 °C ambient')],
      body=lambda: f'''
<section class="two">
 <div>
  <p>I modelled the engine, radiators and coolant tank in Simscape. The model showed that only about 30% of the radiator core was getting useful airflow, which explained why the fans could never be switched off. With the full core in use, it predicted 80–85 °C.</p>
  <p>That result led to a sidepod redesign that ducts all of the air through the core. On the car, coolant came down to <b>85 °C</b> at 20 °C ambient.</p>
 </div>
 <div class="pair">{fig('simulink.png', 'Simscape model of the coolant loop.', contain=True)}{fig('cooling-results.jpg', 'Predicted temperatures with the full core in use.', contain=True)}</div>
</section>
'''),

 dict(slug='lap-time-simulation', title='Lap-time simulation as a design of experiments',
      card='78 vehicle configurations set up and scored in IPG CarMaker to choose the car for the FSUK simulation event.',
      tags=['modelling', 'data'], stat=('78', 'configurations tested'),
      thumb=('svg', 'ipg'),
      role='Performance team', where='UCL Formula Student', when='2022 – 2024',
      tools='IPG CarMaker, Excel',
      lead='For the Formula Student UK lap-time simulation event, each team submits the fastest car it can configure in IPG CarMaker for the dynamic events.',
      nums=[('78', 'configurations set up, 63 completed'), ('244.5', 'best combined score (points)'), ('23rd / 57', 'our result the following year')],
      body=lambda: f'''
<section class="two">
 <div>
  <p>I set up 78 configurations, varying powertrain, aero package, differential, suspension geometry, toe and camber. I scored each one across Acceleration, Skidpad and Sprint and ranked the 63 that completed.</p>
  <p>The ranking also showed which choices mattered. A single motor without the aero package scored highest, and toe and camber separated the top runs. A locked differential was the clear worst. In the following year's event, with a new track and car options, we placed 23rd of 57 teams.</p>
 </div>
 {svgfig('ipg', 'Combined event score of every completed configuration, ranked.', 'chart wide-chart')}
</section>
'''),

 dict(slug='rear-suspension-and-parts', title='Rear suspension and parts for manufacture',
      card='A rear suspension with separate heave and roll dampers, plus the sensor mounts, jigs and parts students had to make themselves.',
      tags=['design'], stat=('2', 'dampers: heave and roll'),
      thumb=('img', 'rear-assembly.jpg'),
      role='Design Engineer', where='UCL Formula Student', when='2022 – 2024',
      tools='Fusion 360, laser cutting, 3D printing',
      lead='Separating heave and roll lets you tune pitch and ride height without changing roll stiffness. I designed the rear suspension around Multimatic heave and roll dampers to do that.',
      nums=[],
      body=lambda: f'''
<section class="two">
 <div>
  <p>Before anything was made, I built a moving kinematic model in Fusion 360 to check the rocker motion and clearances in pure heave and in pure roll.</p>
  <h2>Parts for a student workshop</h2>
  <p>Many of my early parts had to be made by students, fit a crowded chassis and survive a race weekend: suspension travel and brake pressure sensor mounts for the data system, jigs to hold chassis tabs for welding, and a cooling tank I reverse-engineered and modelled.</p>
 </div>
 <div class="pair">{fig('rear-assembly.jpg', 'Full rear assembly with uprights and brakes.')}{fig('rear-rocker.jpg', 'Heave and roll rocker package.')}</div>
</section>
<section class="grid4">
 {fig('sensor-susp.jpg', 'Suspension travel sensor mounts.', contain=True)}
 {fig('sensor-brake.jpg', 'Brake pressure sensor mounts.', contain=True)}
 {fig('jigs.jpg', 'Chassis tab welding jigs.', contain=True)}
 {fig('tank.jpg', 'Cooling tank, modelled in CAD.', contain=True)}
</section>
'''),

 dict(slug='f1-data-python', title='Exploring F1 timing data in Python',
      card='A personal project using the FastF1 library to compare laps and gear use from public F1 telemetry.',
      tags=['data'], stat=None,
      thumb=None, tthumb=('FastF1', 'Python, public F1 telemetry'),
      role='Personal project', where='', when='2024 – present',
      tools='Python, FastF1, matplotlib',
      lead='In my own time I use the FastF1 library to pull public Formula 1 telemetry.',
      nums=[],
      body=lambda: '''
<section class="two">
 <div><p>Two of the scripts I keep coming back to overlay the speed traces of the same driver's fastest qualifying laps at one track in two seasons, with the corners marked, and colour a lap's racing line by the gear in use. Together they show where a car has gained from one year to the next and how differently drivers use the gearbox around a lap.</p></div>
 <div></div>
</section>
'''),
]

EXPERIENCE = [
 ('2026 – now', 'MSc Risk Management & Financial Engineering', 'Imperial College London'),
 ('2025 – 2026', 'Mechanical design placement, Wind Tunnel Engineering', 'Racing Bulls F1'),
 ('2024 – 2025', 'Technical Director', 'UCL Formula Student'),
 ('2024', 'Production methods intern', 'Sweetch Energy, France'),
 ('2023 – 2024', 'Performance Leader and Design Engineer', 'UCL Formula Student'),
 ('2022 – 2026', 'BEng Mechanical Engineering, First Class Honours', 'University College London'),
]

STEPS = ['Define the problem', 'Understand how things work today', 'Design options', 'Agree a direction with the team', 'Simulate and test',
         'Correlate with real data', 'Peer review', 'Implement at the right moment', 'Monitor, then close']

HEAD = lambda title, desc, depth: f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
 <a class="mark" href="{depth}index.html">Ilyes Laraqui Houssaini</a>
 <nav aria-label="Main">
  <a href="{depth}index.html#work">Work</a>
  <a href="{depth}index.html#method">How I work</a>
  <a href="{depth}index.html#about">About</a>
  <a href="{depth}{PDF}" download>PDF portfolio</a>
 </nav>
</header>
'''

FOOT = lambda depth: f'''
<footer class="site" id="contact">
 <div>
  <p class="big">Get in touch</p>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
 </div>
 <ul>
  <li><a href="{LINKEDIN}" rel="me">LinkedIn</a></li>
  <li><a href="{depth}{PDF}" download>Download the PDF portfolio</a></li>
 </ul>
 <p class="small">London, United Kingdom. Racing Bulls work is shown without company images under NDA.</p>
</footer>
</body>
</html>'''


def thumb(p, depth):
    t = p['thumb']
    if t is None:
        big, small = p.get('tthumb', (p['stat'][0], p['stat'][1]) if p['stat'] else ('', ''))
        return f'<div class="thumb text" aria-hidden="true"><span>{big}</span><small>{small}</small></div>'
    if t[0] == 'svg':
        return f'<div class="thumb svgthumb" aria-hidden="true">{SVG(t[1])}</div>'
    contain = ' class="contain"' if t[1].endswith('.png') or 'cooling' in t[1] else ''
    return f'<div class="thumb"><img src="{depth}img/{t[1]}" alt="" loading="lazy"{contain}></div>'


def index():
    cards = []
    for p in PROJECTS:
        tags = ''.join(f'<li>{TAGNAME[t]}</li>' for t in p['tags'])
        stat = f'<p class="stat"><b>{p["stat"][0]}</b> {p["stat"][1]}</p>' if p['stat'] else ''
        cards.append(f'''<li class="project" data-tags="{' '.join(p['tags'])}">
 <a href="projects/{p['slug']}.html">
  {thumb(p, '')}
  <div class="info">
   <h3>{p['title']}</h3>
   <p class="where">{p['where'] or p['role']}{', ' if p['where'] or p['role'] else ''}{p['when']}</p>
   <p>{p['card']}</p>
   <ul class="tags" aria-label="Skills">{tags}</ul>
   {stat}
  </div>
 </a>
</li>''')
    filt = '<button type="button" aria-pressed="true" data-filter="all">All work</button>' + ''.join(
        f'<button type="button" aria-pressed="false" data-filter="{k}">{v}</button>' for k, v in TAGS)
    steps = ''.join(f'<li><span>{s}</span></li>' for s in STEPS)
    exp = ''.join(f'<tr><td>{a}</td><th scope="row">{b}</th><td>{c}</td></tr>' for a, b, c in EXPERIENCE)
    return HEAD('Ilyes Laraqui Houssaini, engineering portfolio',
                'Mechanical engineer working across F1 hardware, vehicle performance, data and quantitative finance.', '') + f'''
<main id="main">
<section class="hero">
 <div class="intro">
  <h1>Ilyes Laraqui<br>Houssaini</h1>
  <p class="lede">I'm a mechanical engineer who likes a support role: using my skills to back up other people's work and help the team succeed. I've designed wind tunnel hardware in Formula 1, led a Formula Student car, and I'm now studying financial engineering at Imperial.</p>
  <p class="cta"><a class="btn" href="#work">See the work</a><a class="btn ghost" href="mailto:{EMAIL}">Email me</a></p>
 </div>
 <table class="titleblock" aria-label="Summary">
  <tr><th scope="row">Now</th><td colspan="3">MSc Risk Management &amp; Financial Engineering, Imperial College London</td></tr>
  <tr><th scope="row">Before</th><td colspan="3">Wind tunnel mechanical design, Racing Bulls F1</td></tr>
  <tr><th scope="row">Degree</th><td colspan="3">BEng Mechanical Engineering, UCL, First Class Honours</td></tr>
  <tr><th scope="row">Works in</th><td colspan="3">Design, data and analysis, modelling and simulation, quantitative finance</td></tr>
  <tr class="foot"><th scope="row">Based</th><td>London</td><th scope="row">Languages</th><td>French, English, German</td></tr>
 </table>
</section>

<section class="work" id="work" aria-labelledby="work-h">
 <div class="workhead">
  <h2 id="work-h">Work</h2>
  <div class="filters" role="group" aria-label="Filter projects by skill">{filt}</div>
  <p class="count" aria-live="polite"><span id="count">{len(PROJECTS)}</span> projects</p>
 </div>
 <ul class="projects">
 {''.join(cards)}
 </ul>
</section>

<section class="method" id="method" aria-labelledby="method-h">
 <h2 id="method-h">How I work</h2>
 <p class="sub">The same loop I've used on wind tunnel parts, suspension, simulation models and a trading strategy.</p>
 <ol class="steps">{steps}</ol>
</section>

<section class="about" id="about" aria-labelledby="about-h">
 <figure class="portrait"><img src="img/vcarb-portrait.jpg" alt="Ilyes kneeling next to the Racing Bulls VCARB 01 show car" loading="lazy"><figcaption>With the VCARB 01 at Racing Bulls</figcaption></figure>
 <div>
  <h2 id="about-h">About</h2>
  <p>I'm French and Moroccan and grew up moving every four years or so: London, Fes, Zurich, Cairo, then back to London. Changing countries that often taught me to settle into new teams quickly and to work across languages.</p>
  <p>My interest in engineering started in a sports car garage in Alsace, where I rebuilt a Porsche 911 engine at 14. Since then I've led a 10+ person Formula Student team as Technical Director, mentored students in UCL's workshop, and judged F1 in Schools.</p>
  <p>Outside work: motorsport strategy and car physics, Rubik's cubes (42 s best), football, basketball and handball, and karate (blue belt).</p>
  <table class="exp"><caption>Experience and education</caption>{exp}</table>
 </div>
</section>
</main>
<script>
(function(){{
 var btns=[].slice.call(document.querySelectorAll('.filters button'));
 var items=[].slice.call(document.querySelectorAll('.project'));
 var count=document.getElementById('count');
 function apply(f){{
  var n=0;
  items.forEach(function(li){{var on=f==='all'||li.dataset.tags.split(' ').indexOf(f)>-1;li.hidden=!on;if(on)n++;}});
  btns.forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.filter===f?'true':'false');}});
  count.textContent=n;
  try{{history.replaceState(null,'',f==='all'?location.pathname:'#'+f);}}catch(e){{}}
 }}
 btns.forEach(function(b){{b.addEventListener('click',function(){{apply(b.dataset.filter);}});}});
 var h=location.hash.slice(1);
 if(['design','data','modelling','quant'].indexOf(h)>-1){{apply(h);}}
}})();
</script>
''' + FOOT('')


def project(i):
    p = PROJECTS[i]
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    tags = ''.join(f'<li><a href="../index.html#{t}">{TAGNAME[t]}</a></li>' for t in p['tags'])
    meta = [('Role', p['role']), ('Where', p['where']), ('When', p['when']), ('Tools', p['tools'])]
    meta = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in meta if b)
    return HEAD(f"{p['title']} – Ilyes Laraqui Houssaini", p['card'], '../') + f'''
<main id="main" class="pj">
 <p class="back"><a href="../index.html#work">All work</a></p>
 <h1>{p['title']}</h1>
 <ul class="tags" aria-label="Skills">{tags}</ul>
 <p class="lede">{p['lead']}</p>
 <dl class="meta">{meta}</dl>
 {nums(p['nums']) if p['nums'] else ''}
 <div class="body">{p['body']()}</div>
 <nav class="pager" aria-label="More projects">
  <a href="{prev_p['slug']}.html"><span>Previous</span>{prev_p['title']}</a>
  <a href="{next_p['slug']}.html"><span>Next</span>{next_p['title']}</a>
 </nav>
</main>
''' + FOOT('../')


if __name__ == '__main__':
    os.makedirs(f'{SITE}/projects', exist_ok=True)
    keep = {p['slug'] + '.html' for p in PROJECTS}
    for f in os.listdir(f'{SITE}/projects'):
        if f.endswith('.html') and f not in keep:
            os.remove(f'{SITE}/projects/{f}')
            print('removed projects/' + f)
    open(f'{SITE}/index.html', 'w').write(index())
    for i, p in enumerate(PROJECTS):
        open(f"{SITE}/projects/{p['slug']}.html", 'w').write(project(i))
    print('built', len(PROJECTS), 'projects')
