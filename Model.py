import tensorflow as tf

#get data from directory of images organized by class label
def create_dataset(directory):
    train_ds = tf.keras.utils.image_dataset_from_directory(
        directory, labels='inferred', label_mode='int', image_size=(64, 64),
        color_mode="grayscale", validation_split=0.2, subset="training", seed=123)

    val_ds = tf.keras.utils.image_dataset_from_directory(
        directory, labels='inferred', label_mode='int', image_size=(64, 64),
        color_mode="grayscale", validation_split=0.2, subset="validation", seed=123)

    return train_ds, val_ds

#build model
def compile_fit(model, train_ds, val_ds):
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

    model.fit(train_ds, validation_data=val_ds, epochs=12)

    return model


def main():
    train_ds, val_ds = create_dataset("Images_By_Label")
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(64, 64)),
        tf.keras.layers.Rescaling(1. / 255),
        tf.keras.layers.Dense(140, activation='relu'),
        tf.keras.layers.Dense(27)
    ])
    model = compile_fit(model, train_ds, val_ds)
    model.save("/tmp/saved_model")