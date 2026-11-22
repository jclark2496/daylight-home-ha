<h1 id="daylight-home">
  <picture>
    <source media="(max-width: 650px)" srcset="docs/readme/cover-mobile.png">
    <img src="docs/readme/cover.png" alt="Daylight Home — blue and rose Home Assistant dashboards with shortcuts for lights, security, climate, and music">
  </picture>
</h1>

<a id="why-daylight-home"></a>

Before bed, open **Lights** to see which rooms still have lights on. Dim one lamp or run your Sleep scene. Daylight Home is a Home Assistant template for the Companion app or a portrait kiosk tablet. You bring the devices and scenes.

**[Set up the dashboard](#quickstart)** · [Walk through a room](#a-look-around) · [Make it yours](#make-it-yours)

## What it can do

- **Home and voice.** See a time-of-day greeting with your first name, initials, and the date. Open Home Assistant Assist from the voice bar, or tap a tile for Lights, Security, Climate, or Music. Each user sees a blue or rose accent.
- **Lights and scenes.** See how many lights are on in the Living Room, Kitchen, Bedroom, and Outside. Open a room to dim one lamp or turn all its lights on or off. The Lights view also runs your Chill, Sleep, and Party scenes.
- **Security.** Check the alarm and both door locks. **Arm home, Arm away, and Disarm send real commands once you connect your alarm. Tapping a door tile toggles that lock.** Hold a door tile to open its details.
- **Climate and music.** Set a target temperature or choose a supported HVAC mode. Both speaker cards show what’s playing. Skip tracks, control playback, set the volume, or mute a speaker.
- **Mobile navigation.** Kiosk Mode hides standard navigation on mobile. The home-screen gear gives you access to the standard interface.

## A look around

**Lights → Living Room** follows one light from the room count to the dimmer. These screens use demo devices on a test instance.

| Find the room | Adjust the light |
| --- | --- |
| <a href="docs/lights.png"><img src="docs/lights.png" width="180" alt="Lights view. Living Room has one of its two lights on."></a> | <a href="docs/living-room.png"><img src="docs/living-room.png" width="180" alt="Living Room view. Main is at 78 percent and Lamp is off."></a> |
| **Living Room** reads “1 of 2 on.” Tap the room tile. | **Main** is on at 78%. Drag its slider to dim it, or tap **All off** to switch off both lights. |

<details>
<summary>See the home screens, security, climate, and music</summary>

The sample home screens use a fictional user. Open a screenshot at full size.

- **Home** — [Blue greeting](docs/home-blue.png) · [Rose greeting](docs/home-rose.png)
- **Security** — [Alarm controls and two door locks](docs/security.png)
- **Climate** — [Thermostat and HVAC modes](docs/climate.png)
- **Music** — [Playback and volume for both speakers](docs/music.png)

</details>

## Requirements

[![Tested on Home Assistant 2026.11.2](https://img.shields.io/badge/Home_Assistant-tested_on_2026.11.2-315ED2)](#requirements)
[![HACS frontend extensions required](https://img.shields.io/badge/HACS-5_frontend_extensions-B21B65)](#requirements)

You’ll need Home Assistant, [HACS](https://hacs.xyz/), and the five frontend extensions below. The template was tested on Home Assistant **2026.11.2** with demo entities on a test instance. Physical-phone and other-version testing is still pending.

| Install through HACS | What it does here |
| --- | --- |
| [button-card](https://github.com/custom-cards/button-card) | Greeting, room tiles, scene chips, and navigation |
| [Mushroom](https://github.com/piitaya/lovelace-mushroom) | Room brightness sliders and speaker controls |
| [card-mod](https://github.com/thomasloven/lovelace-card-mod) | Card styles and spacing |
| [layout-card](https://github.com/thomasloven/lovelace-layout-card) | Grid layout for portrait screens |
| [Kiosk Mode](https://github.com/NemesisRE/kiosk-mode) | Hide standard navigation on mobile |

## Quickstart

1. **Install the five HACS extensions** and refresh your browser or Companion app.
2. **Load the theme.** Copy [daylight.yaml](themes/daylight.yaml) into `/config/themes/`. Restart Home Assistant after first enabling that directory in your frontend configuration. If themes are already enabled, run `frontend.reload_themes`. The [theme setup](SETUP.md#2-theme) includes the YAML.
3. **Create a dashboard** in **Settings → Dashboards** with the URL `daylight-home`. If you choose a different URL, replace the `/daylight-home/` paths in the dashboard YAML.
4. **Connect your entities.** In a copy of [dashboard.yaml](dashboard.yaml), replace the 17 placeholder IDs for lights, scenes, alarm, locks, thermostat, and speakers. The [placeholder table](SETUP.md#4-replace-the-placeholders) lists each one.
5. **Open the dashboard’s Raw configuration editor**, paste your edited YAML, and save. Open `/daylight-home/home`. You should see your name above the four shortcuts. Tap **Lights → Living Room** and check that the two light cards show your devices before trying a control.

The [full setup guide](SETUP.md) includes the tested card versions and installation details.

## One design decision

The four home shortcuts and the room tiles share the `dh_tile` template. It fixes each tile at 104 pixels tall and shortens long labels with an ellipsis. When a room changes from “All off” to “1 of 2 on,” the next row stays in place. [Tile template](dashboard.yaml)

## Make it yours

- **Rooms and devices.** When you add or rename a light, update the room’s `lights` list **and** its subview cards. The list calculates the count on the Lights screen. Also update the room header’s light count and the targets of its All on and All off actions.
- **Blue or rose.** In `dashboard.yaml`, find `button_card_templates → dh_base → variables → rose_users`. Replace the example value with the Home Assistant display names that should use rose, separated by a vertical bar (`|`). Everyone else gets blue.
- **Colors.** Edit [the Daylight theme](themes/daylight.yaml) for the page and standard card colors. The greeting gradients and per-user accents are in [the dashboard YAML](dashboard.yaml). After changing the theme, reload themes. If you change the palette, update the color pairs in [the contrast script](tools/contrast.py) and run `python3 tools/contrast.py` to check normal text, large text, and icons against their respective WCAG thresholds.

## FAQ

**How do I get out of Kiosk Mode?** Tap the gear on the home screen, or open `/daylight-home/home?disable_km`. Hold the gear to go directly to Settings.

**Why does a tile say “Custom element doesn’t exist”?** Check that its extension is installed in HACS and loaded as a dashboard resource. Refresh the browser or clear the Companion app’s frontend cache after installation.

**Why hasn’t the theme changed?** Every view selects `daylight`. Check the file location and the frontend themes include in `configuration.yaml`, then reload themes. If you just enabled themes for the first time, restart Home Assistant. [Theme setup](SETUP.md#2-theme)

**What does the voice bar need?** It opens Home Assistant Assist. Set up a working Assist pipeline on your instance and allow microphone access in the app or browser for spoken requests.

## Credits and license

[![MIT License](https://img.shields.io/badge/license-MIT-315ED2)](LICENSE)

Daylight Home is free to use and adapt under the [MIT License](LICENSE). Thanks to the maintainers of button-card, Mushroom, card-mod, layout-card, and Kiosk Mode. Those extensions are distributed separately under their own licenses.

Daylight Home is an independent community project with no affiliation with Home Assistant, the Open Home Foundation, or the extension authors.

[Daylight Home build notes on Forkthis](https://forkthis.ai/daylight-home/)
