# render_latex.py
import sys
import matplotlib.pyplot as plt
import os

# Make sure the output directory exists

text = sys.argv[1]
output_path = sys.argv[2]

#os.makedirs(os.path.dirname(output_path), exist_ok=True)

fig = plt.figure(figsize=(6.4, 4.8), dpi=400)
fig.text(0.5, 0.5, f'${text}$', ha='center', va='center')
plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)
plt.close(fig)
