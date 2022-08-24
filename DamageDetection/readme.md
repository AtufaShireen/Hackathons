# Damage Detection

## Data Preparation
1. For Handling Imbalanced Dataset
    * performed flips on existing class images with less quantity
    * Added new labels and images to existing dataset
    * performed stratified Split for train , 
    * created categorical encoding for multilabel classfication
    
2. For small dataset
    * performed augmentation
    * performed further image preprocesssing

## Model Building

1. For model training
    * used vgg16 model with imagenet weights.
    * used Dropouts and Regularisation.
    * used sigmoid activation for multilabel classfication

2. For model compilation
    * used adam optimizer
    * used binary loss
    * used fbeta2 for metrics for multilabel classification
    * trained for 80 epochs

3. For monitoring
    * used checkpoints

## Predictions
1. Get the best model from checkpoint
2. Get inverse coding for label outputs
3. used 0.6 threshold for selecting labels
4. monitored fbeta score for selecting threshold

# Extent Of Damage
* same steps as above.
* used same model architecture and its pre-trained weights for detecting extent of damage.
* used categorical loss.
* used precision.
* trained for 40 epochs


# Helper Function
(Refer Example Section)
1. Load imports
2. Run cells of this section
3. run the function predict_image(<image_path>,<model_detect_path>,<model_extent_path>)
Note: 
* detectweights-model is model_detect_path
* extentweights-model is model_extent model_extent_path