import requests
import json
import subprocess
import os

os.chdir("E:\\Alpaca")
while True:
	response = subprocess.check_output(['chat.exe', '-p', 'Give an elaborate description about a vivid, intricately detailed dream a person is experiencing, as if describing an oil painting.'], stderr=subprocess.DEVNULL).decode().strip()
	req_body =  {
		"prompt": response,
		"negative_prompt": "",
		"seed": -1,
		"subseed": -1,
		"subseed_strength": 0,
		"seed_resize_from_h": -1,
		"seed_resize_from_w": -1,
		"sampler_name": "DPM++ SDE Karras",
		"batch_size": 1,
		"n_iter": 1,
		"steps": 40,
		"cfg_scale": 7,
		"width": 512,
		"height": 288,
		"restore_faces": False,
		"tiling": True,
		"do_not_save_samples": False,
		"do_not_save_grid": False,
		"eta": 0,
		"denoising_strength": 0.7,
		"s_min_uncond": 0,
		"s_churn": 0,
		"s_tmax": 0,
		"s_tmin": 0,
		"s_noise": 0,
		"override_settings": {},
		"override_settings_restore_afterwards": True,
		"refiner_switch_at": 0,
		"disable_extra_networks": False,
		"comments": {},
		"enable_hr": True,
		"firstphase_width": 0,
		"firstphase_height": 0,
		"hr_scale": 2.5,
		"hr_upscaler": "Latent",
		"hr_second_pass_steps": 0,
		"hr_resize_x": 1280,
		"hr_resize_y": 720,
		"hr_prompt": "",
		"hr_negative_prompt": "",
		"sampler_index": "DPM++ SDE Karras",
		"script_args": [],
		"send_images": True,
		"save_images": True,
		"alwayson_scripts": {}
	}
	# img2img
	_r = requests.post("http://127.0.0.1:7861/sdapi/v1/txt2img", data=json.dumps(req_body))
