# Pokémon GBA Name Translator

I wanted to play Pokémon ROM hacks with the Pokémon names and attacks in French, so I coded this.
A web-based tool to translate Pokémon names in Game Boy Advance ROMs, specifically designed for Pokémon Emerald. This project allows you to patch ROM files to replace English Pokémon and move names with translated equivalents in any language.

## Features

- **ROM Patcher**: Upload a Pokémon Emerald ROM and automatically replace English names with translated names.
- **Name Translator**: Encode and decode Pokémon names using the game's custom character set.
- **Real-time Progress**: Visual feedback during the patching process.
- **Web-based**: No installation required, works directly in your browser.
- **Customizable**: Modify the translation data files to support any language.

## Files

- `pokemon_emerald_name_patcher.html`: Main patching tool for ROM files.
- `pokemon_name_translater.html`: Utility to encode/decode names to/from hexadecimal.
- `data.js`: Contains the translation dictionaries for Pokémon and moves (currently set to French).
- `data_fr.js`, `data_pkmn_hs.js`, `data_short.js`: Additional data files.
- `fetch_pkmn_data.py`: Python script to fetch and generate translation data.

## Usage

### Patching a ROM

1. Copy `data_fr.js` and rename it to `data.js` in the same directory as `pokemon_emerald_name_patcher.html`. Edit this file to customize translations if needed.
2. Open `pokemon_emerald_name_patcher.html` in your web browser.
3. Click "Choose File" and select your Pokémon Emerald ROM (.gba file).
4. Click "Convertir" to start the patching process.
5. Monitor the progress in the status area.
6. Once complete, click "Télécharger la ROM modifiée" to download the patched ROM.

### Customizing Translations

To translate to a different language:

1. Edit `data.js` to replace the French translations with your desired language.
2. Ensure all translated names use only supported characters (A-Z, space, é, -, ', ., ♂, ♀).
3. The `fetch_pkmn_data.py` script can help generate or update translation data.

## Technical Details

The tool uses a custom character mapping for Pokémon Emerald's font:

- A-Z: 0xBB to 0xD4
- Space: 0x00
- Special characters: é (0x1B), - (0xAE), ' (0xB4), . (0xAD), ♂ (0xB5), ♀ (0xB6)

Names are normalized (uppercase, remove accents) and encoded with proper padding and terminators.

## Requirements

- Modern web browser with File API support
- Python 3.x (for data fetching script)

## License

See LICENSE file for details.

## Disclaimer

This tool is for educational purposes. Ensure you have legal rights to modify ROM files. Backup your original ROM before patching.