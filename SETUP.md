# Daylight Home setup

Tested on a throwaway Home Assistant 2026.11.2 instance with demo and template entities. Cards used: button-card 7.0.1, Mushroom 5.2.3, card-mod 4.2.1, layout-card 2.4.7 and Kiosk Mode 15.0.0. It has not been tested on other versions or on a physical phone.

## 1. HACS prerequisites

In HACS > Frontend, install:

- [ ] **button-card**: [custom-cards/button-card](https://github.com/custom-cards/button-card)
- [ ] **Mushroom**: [piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom). Provides the light and media player cards.
- [ ] **card-mod**: [thomasloven/lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod). Provides `custom:mod-card` and the `card_mod` styles.
- [ ] **layout-card**: [thomasloven/lovelace-layout-card](https://github.com/thomasloven/lovelace-layout-card). Provides `custom:grid-layout`.
- [ ] **Kiosk Mode**: [NemesisRE/kiosk-mode](https://github.com/NemesisRE/kiosk-mode). Hides the header on phones.

After installing, refresh the browser (or clear the Companion app frontend cache).

## 2. Theme

1. Copy `themes/daylight.yaml` to `/config/themes/`.
2. Make sure `configuration.yaml` has:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Restart Home Assistant, or run `frontend.reload_themes`.

Every view sets `theme: daylight`.

## 3. Create the dashboard

1. Go to Settings > Dashboards > **Add dashboard** > "New dashboard from scratch". Use URL **`daylight-home`**.
2. Open the dashboard, then go to edit > three-dot menu > **Raw configuration editor**.
3. Paste in `dashboard.yaml` and save.

To use a different URL, find and replace `/daylight-home/` before pasting.

## 4. Replace the placeholders

| Placeholder | Replace with your... |
|---|---|
| `light.living_room_main`, `light.living_room_lamp` | Living Room lights |
| `light.kitchen_main`, `light.kitchen_island` | Kitchen lights |
| `light.bedroom_main`, `light.bedroom_lamp` | Bedroom lights |
| `light.front_porch`, `light.patio_string` | Outside lights |
| `scene.lights_chill`, `scene.lights_sleep`, `scene.lights_party` | three scenes (the Chill / Sleep / Party chips) |
| `alarm_control_panel.alarm` | alarm panel |
| `lock.front_door_lock`, `lock.back_door_lock` | door locks |
| `climate.thermostat` | thermostat |
| `media_player.speaker`, `media_player.speaker_2` | speakers |
| `Second User\|Another User` (in `dh_base` > `variables` > `rose_users`) | display names that should get the rose accent, separated by `\|` |

When you rename a room or add a light, change both places:

- the room's `lights` list on the Lights view, which drives the "1 of 2 on" label
- the light cards in that room's subview

## 5. Tips

- The hero shows the logged-in user's first name and initials. No photos are used.
- The hero gear opens the dashboard with Kiosk Mode off (`?disable_km`). Long-press the gear to open Settings.
- Every tile has a fixed height, so a tile does not grow when its state label changes.
- `python3 tools/contrast.py` checks the text and accent colors against WCAG contrast.
