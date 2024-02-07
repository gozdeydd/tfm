# Spatial Analysis of the 2023 Earthquakes in Turkiye
This is my master thesis in Master of Data Science in CUNEF supervised by [Diego Bodas Sagi](https://github.com/diegobodas). We had already decided before to work on a spatial data analysis far before this disaster happened. After the disaster we agreed on studying on this as this is also an important business/humanity problem that perhaps AI can create a solution.

## 📧 Contact Information

- **Email**: [![Email](https://img.shields.io/badge/Email-gozdeyzgngl%40gmail.com-blue)](mailto:gozdeyzgngl@gmail.com)
- **GitHub**: [![GitHub](https://img.shields.io/badge/GitHub-gozdeydd-blue?logo=github)](https://github.com/gozdeydd/)
- **LinkedIn**: [![LinkedIn](https://img.shields.io/badge/LinkedIn-Gozde%20Yazganoglu-blue?logo=linkedin)](https://www.linkedin.com/in/gozde-yazganoglu/)


## 1- Problem Description:
On the 6th of February 2023, a series of devastating earthquakes struck the southeast region of Turkey, leaving a profound impact across a vast area. The affected areas included Pazarcik, registering at 7.7 on the Richter scale with coordinates (37.043, 37.288), Elbistan at 7.6 with coordinates (37.239, 38.089), and Nurdagi at 6.6 with coordinates (36.920, 37.304). The repercussions were staggering: 14 million people, equivalent to 16% of the population, were directly affected by the disaster, covering an area of 350,000 km2, roughly the size of Germany. Tragically, the seismic activity resulted in a significant loss of life, with 59,000 reported fatalities spanning both Turkey and Syria, while 122,000 individuals sustained injuries. The economic toll was equally substantial, amounting to a staggering $118.8 billion in valued losses.

## 2- Data Selection and Modeling:

Dataset I have used is composed of several datasets that are spatially joined and merged to have a whole picture.I have used below datasets:

·Copernicus EU Disaster Data

    ·Buildings, Roads, Facilities
    
    ·Campsites
    
    ·Watersources
    
    ·Elevation coutour
    
    ·Area of Interest
    
·TURKSTAT (TUIK)

·ITU -ATAG - Faults Data

·AFAD - Distaster data

## 3- Methods: 
I have used spatial analysis methods such as point pattern analysis, spatial autocorrelation and distance variables to specific regions or points. I have been able to do these analysis thanks to the libraries GeoPandas, PySal, Folium and Contextily. I have referred mostly to the methods described in the [Geographic Data Science with Python](https://geographicdata.science/book/intro.html).

After creation of variables, I have made a supervised multiclass experiment to understand and predict building damage. I have made modeling using PyCaret which is a Auto ML library. This has been a good exploration for its fastness to try several models at a time and feature selection. It also provides quite a lot of visualization of the models.

I also wondered if there are spatial clusters without assigning any dependent variable. Therefore, I also made clustering experiments using again PyCaret. This library has enabled me to test several models. It has been a good exploration after all.

## 4- Map of Repository:
### notebooks: 
1.[01_data_preparation](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/01_data_preparation.ipynb) : Here I read and merge the data to the main dataset.

2.[02_explanatory_data_analysis](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/02_explanatory_data_analisis.ipynb): I do a basic EDA to the big dataset and calculate distance variables.

3.[03_spatial analysis1](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/03_spatial_analisis1.ipynb): I do a poit pattern analysis.

4.[04_spatial analysis2](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/04_spatial_analisis2.ipynb) : I calculate spatial autocorrelations.

5.[05_modeling](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/05_modeling.ipynb) : Supervised modeling experiment and results.

6.[06_clustering](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/06_clustering.ipynb) : Clustering experiments.

[aux_func](https://github.com/gozdeydd/tfm/blob/main/TFM/notebooks/aux_func.py) : Function library.

### html:
This folder has the html versions of the notebooks follow the same structure.

### environments: 
Spatial libraries and Pycaret do not work in the same environment. First 4 notebooks work with new_geo_env which can be found in either [here for pip](https://github.com/gozdeydd/tfm/blob/main/TFM/environments/new_geo_env.txt) or [here for conda](https://github.com/gozdeydd/tfm/blob/main/TFM/environments/new_geo_env.yml)

Modeling and Clustering notebooks should work on [here for pip](https://github.com/gozdeydd/tfm/blob/main/TFM/environments/new_pycaret.txt) or [here for conda](https://github.com/gozdeydd/tfm/blob/main/TFM/environments/new_pycaret.yml)

### documents :
1. [Presentation to the jury](https://github.com/gozdeydd/tfm/blob/main/documents/PresentationSpatialAnalisisOf2023EarthquakesInTurkiye.pdf)
2. [Executive summary](https://github.com/gozdeydd/tfm/blob/main/documents/Spatial%20Analysis%20of%20the%202023%20Earthquakes%20In%20Turkiye-%20An%20Executive%20Summary.pdf)
3. [Thesis](https://github.com/gozdeydd/tfm/blob/main/documents/Spatial%20Analysis%20of%20the%202023%20Earthquakes%20In%20Turkey.pdf)


## 5- Use of the Repository:
I would be more than glad if this repository could help you with your work or learning. I hope also other people can improve it so we can solve some serious problems in the world. 

Please note that this is an academic work if you would like to use it somehow, use proper citations to this work. Do not hesistate to contact to me for further issues.
