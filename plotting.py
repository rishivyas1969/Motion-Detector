from main import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df['Entry_string'] = df['Entry'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['Exit_string'] = df['Exit'].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

plot = figure(width=1000, height=500, x_axis_type='datetime', title='Motion Detector')
plot.yaxis.minor_tick_line_color=None
plot.ygrid.visible = False
plot.yaxis.visible = False

hover = HoverTool(tooltips=[("Entry", "@Entry_string"), ("Exit", "@Exit_string")])
plot.add_tools(hover)

plot_idk=plot.quad(top=1, bottom=0, left="Entry", right="Exit", color="Green", source=cds)
output_file('MotionPlot1.html')
show(plot)