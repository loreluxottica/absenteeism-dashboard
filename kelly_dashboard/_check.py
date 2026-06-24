import ast, sys
sys.path.insert(0, 'C:/Users/muscillol/Desktop/kelly_dashboard')
files = [
    'app.py', 'theme.py',
    'components/charts.py', 'components/weather.py', 'components/kpi_cards.py',
    'pages/forecast.py', 'pages/performance.py', 'pages/landing.py',
]
all_ok = True
for f in files:
    try:
        ast.parse(open(f).read())
        print('OK:', f)
    except SyntaxError as e:
        print('ERR:', f, str(e))
        all_ok = False

# Check no CYAN refs in non-theme files
import re
for f in files:
    if 'theme.py' in f:
        continue
    src = open(f).read()
    if 'theme.CYAN' in src:
        print('CYAN REF FOUND:', f)
        all_ok = False

if all_ok:
    print('ALL CHECKS PASSED')
