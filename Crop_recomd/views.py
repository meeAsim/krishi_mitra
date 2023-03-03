from django.shortcuts import render

from joblib import load
model = load('./model.joblib')


# Create your views here.
def main(request):
    if request.method == 'POST':
        n = request.POST['N']
        N = float(n)
        p = request.POST['P']
        P = float(p)
        po = request.POST['Po']
        Po = float(po)
        te = request.POST['Temp']
        Te = float(te)
        h = request.POST['H']
        H = float(h)
        ph = request.POST['Ph']
        PH = float(ph)
        rf = request.POST['Rf']
        RF = float(rf)
        y_pred=model.predict([[N,P, Po, Te, H, PH, RF]])
        predict = str(y_pred).replace("[","").replace("'","").replace("]","")

        # y_pred = [[N,P, Po, Te, H, PH, RF]]
        if y_pred[0] =='kidneybeans':
            y_pred = 'राज्मा'
            Y_scr = 'https://cdn.shopaccino.com/edible-smart/products/rajma-red-819160_m.jpg?v=446'

        elif y_pred[0] =='rice':
            y_pred = 'rice'
            Y_scr = 'https://free-images.com/lg/4baa/corn_maize_plant_grain.jpg'    
        elif y_pred[0] =='maize':
            y_pred = 'maize'
            Y_scr = 'https://free-images.com/lg/4baa/corn_maize_plant_grain.jpg'    
        elif y_pred[0] =='chickpea':
            y_pred = 'Chickpea'
            Y_scr = 'https://free-images.com/md/5501/chickpea_isolated_india_grain.jpg'    
        elif y_pred[0] =='pigeonpeas':
            y_pred = 'pigeonpeas'
            Y_scr = 'https://imgs.search.brave.com/_sug9PYfGzsONHQGA7qHdemcc2zz-dEEO8FTwqebZZc/rs:fit:872:486:1/g:ce/aHR0cHM6Ly93d3cu/c3BlY2lhbHR5cHJv/ZHVjZS5jb20vc3Bw/aWNzLzExNjUzLnBu/Zw'    
        elif y_pred[0] =='mothbeans':
            y_pred = 'mothbeans'
            Y_scr = 'https://imgs.search.brave.com/D2RzP1kVK2DPARArXVm_OnKPyUyzFnNLnbIKiVsWPpY/rs:fit:800:533:1/g:ce/aHR0cHM6Ly9pbWcy/LmV4cG9ydGVyc2lu/ZGlhLmNvbS9wcm9k/dWN0X2ltYWdlcy9i/Yy1mdWxsL2Rpcl8x/MDMvMzA2OTIzNC9t/b3RoLWJlYW5zLTEx/ODQxMDUuanBn'    
        elif y_pred[0] =='mungbean':
            y_pred = 'mungbean'
            Y_scr = 'https://imgs.search.brave.com/b3vAX-qiV4m_z_0Uechb0LO4v-AtXH8Kb8x6OL-5QtU/rs:fit:900:900:1/g:ce/aHR0cHM6Ly93d3cu/Z291cm1ldGZvb2R3/b3JsZC5jb20vaW1h/Z2VzL1Byb2R1Y3Qv/bGFyZ2UvbXVuZy1i/ZWFucy13aG9sZS1k/cnktMVMtOTU2Lmpw/Zw'    
        elif y_pred[0] =='blackgram':
            y_pred = 'blackgram'
            Y_scr = 'https://imgs.search.brave.com/nQ-nToUWSetMue9GlwJDyYf7cW-r-5mVlMAmxfQaL9w/rs:fit:898:888:1/g:ce/aHR0cHM6Ly93d3cu/bmV0bWVkcy5jb20v/aW1hZ2VzL2Ntcy93/eXNpd3lnL2Jsb2cv/MjAxOS8wOS9CbGFj/a0dyYW1fYmlnXzEu/anBn'    
        elif y_pred[0] =='lentil':
            y_pred = 'lentil'
            Y_scr = 'https://free-images.com/lg/d583/lentils_chana_pappu_paripu_0.jpg'    
        elif y_pred[0] =='pomegranate':
            y_pred = 'pomegranate'
            Y_scr = 'https://free-images.com/md/c0a8/pomegranate_pomegranate_seeds_close.jpg'    
        elif y_pred[0] =='banana':
            y_pred = 'banana'
            Y_scr = 'https://free-images.com/md/abb1/banana_tree_bananas_shrub_0.jpg'    
        elif y_pred[0] =='mango':
            y_pred = 'mango'
            Y_scr = 'https://free-images.com/md/719d/mango_mango_tree_fruits.jpg'    
        elif y_pred[0] =='grapes':
            y_pred = 'grapes'
            Y_scr = 'https://free-images.com/md/c434/grapes_green_grapes_nature_0.jpg'    
        elif y_pred[0] =='watermelon':
            y_pred = 'watermelon'
            Y_scr = 'https://free-images.com/lg/9165/watermelon_hybrid_watermelon_seed.jpg'    
        elif y_pred[0] =='muskmelon':
            y_pred = 'muskmelon'
            Y_scr = 'https://free-images.com/md/e433/cantaloupes_muskmelons.jpg'    
        elif y_pred[0] =='apple':
            y_pred = 'apple'
            Y_scr = 'https://free-images.com/md/f36d/apple_red_boskoop_boskoop.jpg'    
        elif y_pred[0] =='orange':
            y_pred = 'orange'
            Y_scr = 'https://free-images.com/md/8f3d/orange_fruit_orange_tree_14.jpg'    
        elif y_pred[0] =='papaya':
            y_pred = 'papaya'
            Y_scr = 'https://free-images.com/md/6614/papaya_fruit_exotic_papaya.jpg'    
        elif y_pred[0] =='coconut':
            y_pred = 'coconut'
            Y_scr = 'https://free-images.com/md/7a64/coconut_coconut_trees_1036198.jpg'    
        elif y_pred[0] =='cotton':
            y_pred = 'cotton'
            Y_scr = 'https://free-images.com/md/67ed/cotton_crop_cotton_tree.jpg'    
        elif y_pred[0] =='jute':
            y_pred = 'jute'
            Y_scr = 'https://free-images.com/md/05bc/jute_string_for_macro.jpg'    
        elif y_pred[0] =='coffee':
            y_pred = 'coffee'
            Y_scr = 'https://free-images.com/lg/7358/coffee_beans_ripe_agriculture.jpg'    
       
        else:
            y_pred = 'sorry' 
            Y_scr = 'https://c.pxhere.com/photos/69/8e/corn_food_organic_healthy_agriculture-451399.jpg!d'      
        print(y_pred)

        return render(request, 'index.html',{'result' :y_pred, 'src': Y_scr})
    return render(request, 'index.html')    