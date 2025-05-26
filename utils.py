import os

def create_output_directories():
    """
    Create necessary directories for audio files and transcripts
    """
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Define directories
    audio_dir = os.path.join(project_root, "audio_files")
    output_dir = os.path.join(project_root, "transcripts")
    
    # Create directories if they don't exist
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    return audio_dir, output_dir

def get_audio_files(audio_dir):
    """
    Get list of supported audio files in the audio directory
    """
    supported_formats = ('.mp3', '.wav', '.m4a', '.flac')
    audio_files = []
    
    for file in os.listdir(audio_dir):
        if file.lower().endswith(supported_formats):
            audio_files.append(os.path.join(audio_dir, file))
    
    return audio_files


