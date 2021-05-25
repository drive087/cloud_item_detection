# Computer vision project
## Cashierless Application

Our application is trying solve the problem of waiting in a queue for a while in the supermarket when checking out. Moreover, according to the covid-19 situation nowadays, it would be better if we could reduce the risk when customers exposes to the staff at the cashier. We apply computer vision knowledge as desribed in the following procedures.

1. Use the camera to scan the products (multiple products can be scaned at the same time).
2. Find contour to get the bounding box of each product, then each bounding box is an item passed to the model in 3.
3. Model to classify the item in order to get its price, in this case we use Few-shot learning model.
4. Calculate total summary and send it to user's email.

### Technical Challenges
1. New items can be added to the system
2. Multiple products are checked out at the same time

### Related Works
1. Amazon Go Grocery, Seattle
	- Shoppers scan a smartphone app to enter the store
	- Cameras and sensors track what's taken off shelves
	- Items are charged to an Amazon account after leaving
	- Limitation of this method to our project: we only have 1 camera

2. Computer Vision Powers Cashier-less Checkout (From https://www.abtosoftware.com/blog/abto-golden-line)
	- Deep learning-based model training: Object detection and classification by training a custom deep learning-based model
	- Cashier-less checkout video processing: Installing the standard camera above the checkout conveyor – no additional sensors are needed
	- Limitation of this method to our project: When the new product is added to the dataset, the whole model has to be fine tuned.

### Method and Results
1. Data creation
	- Take photos of the products
	- Padding the photos to make them all the same image size
2. Training Model
	- Few-shot learning with Prototypical Networks
3. Image processing
	- Take photos of the background
	- Use background subtraction for capture item in frame
	- Find contour of item and create bounding box
4. Classification
	- Use model to predict item in the bounding box
	- And send the prediction to the server for price calculation
5. Evaluation
	- Dataset: 9 classes of created grocery dataset
	- Metric: Accuracy
	- Result: 100% accurary

### Discussion and Future Work
- Each item cannot be adjacent to each other because we use traditional CV to crop a object.
- Try to use some other segmentation instead of traditional methods to solve the limitation.
- The linkage between application’s authentication  and the cashierless checkout has to be created to handle more than 1 users.


###  Video URL
The video introducing this project is available at: https://www.youtube.com/watch?v=Cvn_HZuV8eg

### HOW TO
1. conda env create -f environment.yml 
2. conda activate <your env name>
2. python main_add_item_2_train.py (Capture background image for image processing-click BG, p.s.this program needed plain background for good perform)
3. python main.py (Don't forget to change endpoint variable to yours)
4. something wrong contact me - thus.kanj@gmail.com 
