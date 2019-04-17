
- **Download [pre-trained model](https://drive.google.com/uc?id=1OZgzVYTLXSK4-CuFV6z1rtMKtHv-AFLc&export=download)** . Replace the models folder with this folder.
**Download [pre-trained model](https://drive.google.com/uc?id=1M2Rxr2IyHuV_3yHgvz5FqWKYUF1BVX58&export=download)** . Replace the data folder with this folder.
- **Run the chatbot**. Open a terminal session and run `python3 gui.py`.


 
- **Provide your own training data.** Training data should be one or more newline-delimited text files. Each line of dialogue should begin with "> " and end with a newline. You'll need a lot of it. Several megabytes of uncompressed text is probably the minimum, and even that may not suffice if you want to train a large model. Text can be provided as raw .txt files or as bzip2-compressed (.bz2) files.

### Train your own model

- **Train.** Use `train.py` to train the model. The default hyperparameters are the best that I've found, and are what I used to train the pre-trained model for a couple of months. These hyperparameters will just about fill the memory of a GTX 1080 Ti GPU (11 GB of VRAM), so if you have a smaller GPU, you will need to adjust them accordingly (for example, set --num_blocks to 2).

  Training can be interrupted with crtl-c at any time, and will immediately save the model when interrupted. Training can be resumed on a saved model and will automatically carry on from where it was interrupted.
