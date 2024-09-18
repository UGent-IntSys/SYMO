## Helpers for CNNs

## Plot the model history including the validation 
def plot_model_history_val (history_model):
    fig, (ax2, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))
    # loss
    ax1.plot(history_model.history['loss'], label='Train Loss')
    ax1.plot(history_model.history['val_loss'], label='Validation Loss')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.legend()

    # accuracy
    ax2.plot(history_model.history['accuracy'], label='Train Accuracy')
    ax2.plot(history_model.history['val_accuracy'], label='Validation Accuracy')
    ax2.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.legend()