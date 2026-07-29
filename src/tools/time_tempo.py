"""Time signature, tempo, and key signature tools for MuseScore MCP."""

from ..client import MuseScoreClient


def setup_time_tempo_tools(mcp, client: MuseScoreClient):
    """Setup time signature, tempo, and key signature tools."""
    
    @mcp.tool()
    async def set_time_signature(numerator: int = 4, denominator: int = 4):
        """Set the time signature.
        
        Args:
            numerator: Top number of time signature (beats per measure)
            denominator: Bottom number of time signature (note value that gets the beat)
        """
        return await client.send_command("setTimeSignature", {
            "numerator": numerator,
            "denominator": denominator
        })
    
    @mcp.tool()
    async def set_tempo(bpm: int = 120):
        """Set the tempo of the score.
        
        Args:
            bpm: Beats per minute (e.g., 120)
        """
        return await client.send_command("setTempo", {"bpm": bpm})

    @mcp.tool()
    async def add_key_signature(fifths: int):
        """Add a key signature change at the current cursor position.
        
        Args:
            fifths: Number of accidentals on the circle of fifths (-7 to 7,
                   negative for flats, positive for sharps, 0 = C major/A minor)
        """
        return await client.send_command("setKeySignature", {"fifths": fifths})