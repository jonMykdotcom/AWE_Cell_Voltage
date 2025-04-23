This is my Thesis project where i aim to predict the cell voltage during alkaline water electrolysis based on Zirfon diaphragm separator. 
The input parameters are as follows:
1. Temperature (oC)
2. Pressure (Bar)
3. Potassium hydroxide concentration (wt%)
4. Electrodes gap (mm)
5. Current density (a/cm^2)

Output:
1. Cell Voltage (V)
# AWE_Cell_Voltage
ML Modelling of Alkaline Water Electrolysis Cell Voltage

Following up the workflow on the Youtube channel below:
https://www.youtube.com/watch?v=S_F_c9e2bz4&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG
Create Main folder. Link the Main Folder to a Git and Github.
Main Folder Name: Cell Voltage
    	Files:
        o	.gitignore
        o	README.md
        o	requirements.txt
        o	app.py
        o	setup.py
    	Folders: 
        o	.venv
        o	src
            	Files:
            •	__init__.py
            •	logger.py
            •	utils.py
            •	exception.py
            	Folders
                •	components
                    o	Files:
                    	__init__.py
                    	data_ingestion.py
                    	data_transformation.py
                    	model_trainer.py
                •	pipeline
                    o	Files:
                    	__init__.py
                    	train_pipeline.py
                    	predict_pipeline.py
	
    o	notebooks
        	Files:
        •	Cell_Voltage_EDA_9Mar.ipynb
        •	Cell_Voltage_EDA_21Apr.ipynb
        •	Cell_Voltage_Data_Aggregation.ipynb
        •	Model_Train.ipynb
        	Folders
        •	data
            o	Files:
            	Cell_Voltage.xlsx
	

ML Workflow
Problem Statement > Data Collection > Data Checks >EDA> Preprocessing>Model Training> Best Model
