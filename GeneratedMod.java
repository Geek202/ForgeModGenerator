package me.geek.tom.${modid};

import net.minecraftforge.fml.StartupMessageManager;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod(GeneratedMod.MODID)
public class GeneratedMod {
    
	public static final String MODID = "${modid}";
	
	public GeneratedMod() {
		FMLJavaModLoadingContext.get().getModEventBus().addListener(this::init);
	}
	
	private void init(final FMLCommonSetupEvent event) {
		StartupMessageManager.addModMessage("GeneratedMod::init");
	}
}
