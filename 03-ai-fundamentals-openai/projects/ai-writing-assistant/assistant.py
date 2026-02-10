"""
AI Writing Assistant - Combines all Phase 3 concepts
"""
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken

load_dotenv()
client = OpenAI()

MODES = {
    "creative": "You are a creative writer. Use vivid language and engaging narratives.",
    "technical": "You are a technical writer. Be precise, clear, and structured.",
    "simple": "You explain things simply using everyday language."
}

class WritingAssistant:
    def __init__(self):
        self.mode = "creative"
        self.messages = []
        self.total_tokens = 0
        self.encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        self.reset_conversation()
    
    def reset_conversation(self):
        self.messages = [{"role": "system", "content": MODES[self.mode]}]
    
    def change_mode(self, mode: str):
        if mode in MODES:
            self.mode = mode
            self.reset_conversation()
            print(f"✓ Mode changed to: {mode}")
        else:
            print(f"✗ Invalid mode. Options: {', '.join(MODES.keys())}")
    
    def stream_response(self, user_input: str):
        self.messages.append({"role": "user", "content": user_input})
        
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            stream=True
        )
        
        full_response = ""
        print("\nAssistant: ", end='', flush=True)
        
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                full_response += delta
                print(delta, end='', flush=True)
        
        print()
        self.messages.append({"role": "assistant", "content": full_response})
        
        tokens = len(self.encoding.encode(user_input + full_response))
        self.total_tokens += tokens
        print(f"\n[{tokens} tokens]")
    
    def show_stats(self):
        print(f"\nStatistics:")
        print(f"  Mode: {self.mode}")
        print(f"  Total tokens: {self.total_tokens}")
        print(f"  Messages: {len(self.messages)}")
        print(f"  Approx cost: ${self.total_tokens / 1000 * 0.002:.4f}")
    
    def run(self):
        print("🤖 AI Writing Assistant")
        print(f"Mode: {self.mode} | Commands: /mode, /stats, /clear, quit")
        print("=" * 60)
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("\n👋 Goodbye!")
                break
            
            if user_input.startswith('/mode '):
                mode = user_input.split(' ', 1)[1]
                self.change_mode(mode)
                continue
            
            if user_input == '/stats':
                self.show_stats()
                continue
            
            if user_input == '/clear':
                self.reset_conversation()
                self.total_tokens = 0
                print("✓ Conversation cleared!")
                continue
            
            try:
                self.stream_response(user_input)
            except Exception as e:
                print(f"\n✗ Error: {e}")

if __name__ == "__main__":
    assistant = WritingAssistant()
    assistant.run()
