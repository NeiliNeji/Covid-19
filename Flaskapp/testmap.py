import hvplot.pandas
import hvplot
import matplotlib
from multiprocessing import Process
import pandas as pd
import geopandas
import numpy as np
from bokeh.embed import file_html
import holoviews as hv
from bokeh.resources import CDN, INLINE
from bokeh.embed import components
from bokeh.models import FixedTicker
from DataPreprocessing_Global_Map import get_map_data
geopandas.datasets.available
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
merge=get_map_data().copy()
merge.replace('Western Sahara', 'W. Sahara', inplace = True)
merge.replace('US', 'United States of America', inplace = True)
merge.replace('Congo (Kinshasa)', 'Dem. Rep. Congo', inplace = True)
merge.replace('Dominican Republic', 'Dominican Rep.', inplace = True)
merge.replace('Falkland Islands (Malvinas)', 'Falkland Is.', inplace = True)
merge.replace("Cote d'Ivoire", "Côte d'Ivoire", inplace = True)
merge.replace('Central African Republic', 'Central African Rep.', inplace = True)
merge.replace('Congo (Brazzaville)', 'Congo', inplace = True)
merge.replace('Equatorial Guinea', 'Eq. Guinea', inplace = True)
merge.replace('Eswatini', 'eSwatini', inplace = True)
merge.replace('West Bank and Gaza', 'Palestine', inplace = True)
merge.replace('Burma', 'Myanmar', inplace = True)
merge.replace('Korea, South', 'South Korea', inplace = True)
merge.replace('Taiwan*', 'Taiwan', inplace = True)
merge.replace('Bosnia and Herzegovina', 'Bosnia and Herz.', inplace = True)
merge.replace('North Macedonia', 'Macedonia', inplace = True)
merge.replace('Cyprus', 'N. Cyprus', inplace = True)
merge.replace('South Sudan', 'S. Sudan', inplace = True)

world_map = world.merge(merge, left_on=['name'], right_on=['Countries'])

def map_active_percent():

    ax=world_map.hvplot(c="Active Percent",
                                    hover_cols=[ 'Active','Countries'],
                                 width=900,height=500,
                                 title="World Map Active/Population %"
                                ).options(
    color_levels=[0,0.1,0.2,0.3,0.4,4.0] , cmap=["#228B22","#90EE90","#ff7f00","#FF0000","#800000"],  colorbar=True, width=900,colorbar_opts={'ticker': FixedTicker(ticks=[0.1,0.2,0.3,0.4]),'major_label_overrides': {
            0.1: '  0.1%', 
            0.2: '  0.2%', 
            0.3: '  0.3%',
            0.4: '0.4%'
        },})
    p = hv.render(ax, backend='bokeh')
    return(p)


def map_active():

    ax=world_map.hvplot(c="Active",
                                    hover_cols=[ 'Countries','Confirmed'],
                                 width=900,height=500,
                                 title="World Map Active Cases"
                                ).options(color_levels=[0,100000,200000, 500000, 1000000,6000000],colorbar_opts={'ticker': FixedTicker(ticks=[100000,200000, 500000, 1000000]),'major_label_overrides': {
            100000: '  100000', 
            200000: '  200000', 
            500000: '  500000',
            1000000: '1M'
        },} , cmap=["#228B22","#FFF840","#ff7f00","#FF0000","#800000"],  colorbar=True, width=900)


    p = hv.render(ax, backend='bokeh')
    return(p)
