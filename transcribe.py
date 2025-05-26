import whisper 
import os
from utils import create_output_directories, get_audio_file, get_audio_files

def load_model(model_size="base"):
    """
    Load the Whisper model.
    model_size options: tiny, base, small, medium, large
    """
    print(f"Loading Whisper model ({model_size})...")
    return whisper.load_model(model_size)

def transcribe_audio(model, audio_path, output_dir):
    """
    Transcribe a single audio file and save the result
    """
    print(f"Transcribing: {os.path.basename(audio_path)}")
    
    # Perform transcription
    result = model.transcribe(audio_path)
    
    # Create output filename
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_transcript.txt")
    
    # Save transcription
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"Transcription saved to: {output_path}")
    return output_path

def main():
    # Create necessary directories
    audio_dir, output_dir = create_output_directories()
    
    # Load the model
    model = load_model("base")
    
    # Get list of audio files
    audio_files = get_audio_files(audio_dir)
    print(audio_dir,output_dir)
    if not audio_files:
        print("No audio files found in the audio_files directory!")
        return
    
    # Process each audio file
    for audio_file in audio_files:
        try:
            transcribe_audio(model, audio_file, output_dir)
        except Exception as e:
            print(f"Error processing {audio_file}: {str(e)}")
    
    print("Transcription complete!")

if __name__ == "__main__":
    main()
