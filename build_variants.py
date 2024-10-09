from apkmirror import Version
from utils import move_merged_apk, rename_apk, patch_revanced_apk, patch_xposed_apk


def build_apks(latest_version: Version):
    # patch
    apk = "big_file_merged.apk"
    integrations = "bins/integrations.apk"
    patches = "bins/patches.jar"
    cli = "bins/cli.jar"
    xposed = "bins/xposed.apk"
    lspatch = "bins/lspatch.jar"
    apkrenamer = "bins/apkrenamer/renamer.jar"
    output_list = []

    rename_apk(
        apkrenamer,
        apk,
        out="revenge-discord-renamed.apk"
        name="Revenge",
        package="io.github.revenge.app",
        icon="icons/revenge-discord.png",
        files=output_list
    )

    patch_xposed_apk(
        lspatch,
        xposed,
        apk="revenge-discord-renamed.apk",
        out_dir="revenge-discord",
        out=f"discord-revenge-v{latest_version.version}.apk",
        files=output_list
    )

    rename_apk(
        apkrenamer,
        apk,
        out="bunny-discord-renamed.apk"
        name="Bunny",
        package="io.github.bunny.app",
        icon="icons/bunny-discord.png",
        files=output_list
    )

    patch_xposed_apk(
        lspatch,
        xposed,
        apk="bunny-discord-renamed.apk",
        out_dir="bunny-discord",
        out=f"discord-bunny-v{latest_version.version}.apk",
        files=output_list
    )

    move_merged_apk(
        apk,
        out=f"discord-merged-v{latest_version.version}.apk",
        files=output_list
    )
    
    return output_list
