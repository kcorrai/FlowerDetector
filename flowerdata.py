import pandas as pd

df = pd.read_excel('flower_data.xlsx')

def flowerdataset(user):
    flower_name = user
    color = df.loc[df['Name'] == flower_name, 'Color'].values[0]
    petal_Count = df.loc[df['Name'] == flower_name, 'Petal_Count'].values[0]
    bloom_Season = df.loc[df['Name'] == flower_name, 'Bloom_Season'].values[0]
    height_cm = df.loc[df['Name'] == flower_name, 'Height_cm'].values[0]
    info = df.loc[df['Name'] == flower_name, 'Info'].values[0]
    latin_name = df.loc[df['Name'] == flower_name, 'Latin_Name'].values[0]
    common_use = df.loc[df['Name'] == flower_name, 'Common_Use'].values[0]
    growing_conditions = df.loc[df['Name'] == flower_name, 'Growing_Conditions'].values[0]
            
    return flower_name, color, petal_Count, bloom_Season, height_cm, info, latin_name, common_use, growing_conditions

image_names = {'Rose': '../static/img/flowertypes/rose.jpg',
                'Tulip': '../static/img/flowertypes/tulip.jpg',
                'Sunflower': '../static/img/flowertypes/sunflower.jpg',
                'Daffodil': '../static/img/flowertypes/daffodil.jpg' ,
                'Lily': '../static/img/flowertypes/lily.jpg',
                'Orchid': '../static/img/flowertypes/orchid.jpg',
                'Marigold': '../static/img/flowertypes/marigold.jpg',
                'Daisy': '../static/img/flowertypes/daisy.jpg',
                'Lavender': '../static/img/flowertypes/lavender.png',
                'Peony': '../static/img/flowertypes/peony.jpg',
                'Iris': '../static/img/flowertypes/ıris.jpg',
                'Chrysanthemum': '../static/img/flowertypes/chrysanthemum.jpg',
                'Poppy': '../static/img/flowertypes/poppy.jpg',
                'Hyacinth': '../static/img/flowertypes/hyacinth.jpeg',
                'Carnation': '../static/img/flowertypes/carnation.jpg'
}


    