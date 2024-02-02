import streamlit as st
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2




# Set up gRPC channel for NewsGuardian model
channel_tts = ClarifaiChannel.get_grpc_channel()
stub_tts = service_pb2_grpc.V2Stub(channel_tts)
metadata_tts = (('authorization', 'Key ' + PAT_TTS),)
userDataObject_tts = resources_pb2.UserAppIDSet(user_id=USER_ID_TTS, app_id=APP_ID_TTS,)

# Streamlit app
st.title("NewsGuardian")


# Inserting logo
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdA-MJ_SUCRgLs1prqudpMdaX4x-x10Zqlwp7cpzXWCMM9xjBAJYWdJsDlLoHBqNpj8qs&usqp=CAU")
# Function to get gRPC channel for NewsGuardian model
def get_tts_channel():
    channel_tts = ClarifaiChannel.get_grpc_channel()
    return channel_tts, channel_tts.metadata



# User input
model_type = st.selectbox("Select Model", ["NewsGuardian model","NewsGuardian model"])
raw_text = st.text_area("This news is real or fake?")
image_upload = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Button to generate result
if st.button("NewsGuardian News Result"):
    if model_type == "NewsGuardian model":
        # Set up gRPC channel for NewsGuardian model
        channel_gpt4 = ClarifaiChannel.get_grpc_channel()
        stub_gpt4 = service_pb2_grpc.V2Stub(channel_gpt4)
        metadata_gpt4 = (('authorization', 'Key ' + PAT_GPT4),)
        userDataObject_gpt4 = resources_pb2.UserAppIDSet(user_id=USER_ID_GPT4, app_id=APP_ID_GPT4)

        # Prepare the request for NewsGuardian model
        input_data_gpt4 = resources_pb2.Data()

        if raw_text:
            input_data_gpt4.text.raw = raw_text

        if image_upload is not None:
            image_bytes_gpt4 = image_upload.read()
            input_data_gpt4.image.base64 = image_bytes_gpt4

        post_model_outputs_response_gpt4 = stub_gpt4.PostModelOutputs(
            service_pb2.PostModelOutputsRequest(
                user_app_id=userDataObject_gpt4,
                model_id=MODEL_ID_GPT4,
                version_id=MODEL_VERSION_ID_GPT4,
                inputs=[resources_pb2.Input(data=input_data_gpt4)]
            ),
            metadata=metadata_gpt4  # Use metadata directly in the gRPC request
        )

        # Check if the request was successful for NewsGuardian model
        if post_model_outputs_response_gpt4.status.code != status_code_pb2.SUCCESS:
            st.error(f"NewsGuardian model API request failed: {post_model_outputs_response_gpt4.status.description}")
        else:
            # Get the output for NewsGuardian model
            output_gpt4 = post_model_outputs_response_gpt4.outputs[0].data

            # Display the result for NewsGuardian model
            if output_gpt4.HasField("image"):
                st.image(output_gpt4.image.base64, caption='Generated Image (NewsGuardian model)', use_column_width=True)
            elif output_gpt4.HasField("text"):
                # Display the text result
                st.text(output_gpt4.text.raw)

                # Convert text to speech and play the audio
                stub_tts = service_pb2_grpc.V2Stub(channel_gpt4)  # Use the same channel for TTS

                tts_input_data = resources_pb2.Data()
                tts_input_data.text.raw = output_gpt4.text.raw

                tts_response = stub_tts.PostModelOutputs(
                    service_pb2.PostModelOutputsRequest(
                        user_app_id=userDataObject_tts,
                        model_id=MODEL_ID_TTS,
                        version_id=MODEL_VERSION_ID_TTS,
                        inputs=[resources_pb2.Input(data=tts_input_data)]
                    ),
                    metadata=metadata_gpt4  # Use the same metadata for TTS
                )

                # Check if the TTS request was successful
                if tts_response.status.code == status_code_pb2.SUCCESS:
                    tts_output = tts_response.outputs[0].data
                    st.audio(tts_output.audio.base64, format='audio/wav')
                else:
                    st.error(f"NewsGuardian model API request failed: {tts_response.status.description}")

    elif model_type == "DALL-E":
        # Set up gRPC channel for DALL-E
        channel_dalle = ClarifaiChannel.get_grpc_channel()
        stub_dalle = service_pb2_grpc.V2Stub(channel_dalle)
        metadata_dalle = (('authorization', 'Key ' + PAT_DALLE),)
        userDataObject_dalle = resources_pb2.UserAppIDSet(user_id=USER_ID_DALLE, app_id=APP_ID_DALLE)

        # Prepare the request for DALL-E
        input_data_dalle = resources_pb2.Data()

        if raw_text:
            input_data_dalle.text.raw = raw_text

        post_model_outputs_response_dalle = stub_dalle.PostModelOutputs(
            service_pb2.PostModelOutputsRequest(
                user_app_id=userDataObject_dalle,
                model_id=MODEL_ID_DALLE,
                version_id=MODEL_VERSION_ID_DALLE,
                inputs=[resources_pb2.Input(data=input_data_dalle)]
            ),
            metadata=metadata_dalle
        )

        # Check if the request was successful for DALL-E
        if post_model_outputs_response_dalle.status.code != status_code_pb2.SUCCESS:
            st.error(f"DALL-E API request failed: {post_model_outputs_response_dalle.status.description}")
        else:
            # Get the output for DALL-E
            output_dalle = post_model_outputs_response_dalle.outputs[0].data

            # Display the result for DALL-E
            if output_dalle.HasField("image"):
                st.image(output_dalle.image.base64, caption='Generated Image (DALL-E)', use_column_width=True)
            elif output_dalle.HasField("text"):
                st.text(output_dalle.text.raw)

    elif model_type == "NewsGuardian model":
        # Set up gRPC channel for NewsGuardian model
        channel_tts = ClarifaiChannel.get_grpc_channel()
        stub_tts = service_pb2_grpc.V2Stub(channel_tts)
        metadata_tts = (('authorization', 'Key ' + PAT_TTS),)
        userDataObject_tts = resources_pb2.UserAppIDSet(user_id=USER_ID_TTS, app_id=APP_ID_TTS)

        # Prepare the request for NewsGuardian model
        input_data_tts = resources_pb2.Data()

        if raw_text:
            input_data_tts.text.raw = raw_text

        post_model_outputs_response_tts = stub_tts.PostModelOutputs(
            service_pb2.PostModelOutputsRequest(
                user_app_id=userDataObject_tts,
                model_id=MODEL_ID_TTS,
                version_id=MODEL_VERSION_ID_TTS,
                inputs=[resources_pb2.Input(data=input_data_tts)]
            ),
            metadata=metadata_tts
        )

        # Check if the request was successful for NewsGuardian model
        if post_model_outputs_response_tts.status.code != status_code_pb2.SUCCESS:
            st.error(f"NewsGuardian model API request failed: {post_model_outputs_response_tts.status.description}")
        else:
            # Get the output for NewsGuardian model
            output_tts = post_model_outputs_response_tts.outputs[0].data

            # Display the result for NewsGuardian model
            if output_tts.HasField("text"):
                st.text(output_tts.text.raw)

            if output_tts.HasField("audio"):
                st.audio(output_tts.audio.base64, format='audio/wav')


# Add the beautiful social media icon section
st.markdown("""
  <div align="center">
      <a href="https://github.com/pyresearch/pyresearch" style="text-decoration:none;">
        <img src="https://user-images.githubusercontent.com/34125851/226594737-c21e2dda-9cc6-42ef-b4e7-a685fea4a21d.png" width="2%" alt="" /></a>
      <img src="https://user-images.githubusercontent.com/34125851/226595799-160b0da3-c9e0-4562-8544-5f20460f7cc9.png" width="2%" alt="" />
        <a href="https://www.linkedin.com/company/pyresearch/" style="text-decoration:none;">
        <img src="https://user-images.githubusercontent.com/34125851/226596446-746ffdd0-a47e-4452-84e3-bf11ec2aa26a.png" width="2%" alt="" /></a>
      <img src="https://user-images.githubusercontent.com/34125851/226595799-160b0da3-c9e0-4562-8544-5f20460f7cc9.png" width="2%" alt="" />
      <a href="https://twitter.com/Noorkhokhar10" style="text-decoration:none;">
        <img src="https://user-images.githubusercontent.com/34125851/226599162-9b11194e-4998-440a-ba94-c8a5e1cdc676.png" width="2%" alt="" /></a>
      <img src="https://user-images.githubusercontent.com/34125851/226595799-160b0da3-c9e0-4562-8544-5f20460f7cc9.png" width="2%" alt="" />    
      <a href="https://www.youtube.com/@Pyresearch" style="text-decoration:none;">
        <img src="https://user-images.githubusercontent.com/34125851/226599904-7d5cc5c0-89d2-4d1e-891e-19bee1951744.png" width="2%" alt="" /></a>
      <img src="https://user-images.githubusercontent.com/34125851/226595799-160b0da3-c9e0-4562-8544-5f20460f7cc9.png" width="2%" alt="" />
      <a href="https://www.facebook.com/Pyresearch" style="text-decoration:none;">
        <img src="https://user-images.githubusercontent.com/34125851/226600380-a87a9142-e8e0-4ec9-bf2c-dd6e9da2f05a.png" width="2%" alt="" /></a>
      <img src="https://user-images.githubusercontent.com/34125851/226595799-160b0da3-c9e0-4562-8544-5f20460f7cc9.png" width="2%" alt="" />
      <a href="https://www.instagram.com/pyresearch/" style="text-decoration:none;">  
        <img src="https://user-images.githubusercontent.com/34125851/226601355-ffe0b597-9840-4e10-bbef-43d6c74b5a9e.png" width="2%" alt="" /></a>      
  </div>
  <hr>
""", unsafe_allow_html=True)






