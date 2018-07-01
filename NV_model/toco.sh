toco --input_file=graph.pbtxt \
--input_format=TENSORFLOW_GRAPHDEF \
--output_format=TFLITE \
--output_file=tflite.tflite \
--inference_type=FLOAT \
--input_type=FLOAT \
--input_arrays=input
