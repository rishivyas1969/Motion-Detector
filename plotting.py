from main import df
from bokeh.plotting import figure, output_file, show

plot = figure(width=1000, height=500, x_axis_type='datetime', title='Motion Detector')
plot_idk=plot.quad(top=1, bottom=0, left=df['Entry'], right=df['Exit'], color="Green")
output_file('MotionPlot.html')
show(plot)