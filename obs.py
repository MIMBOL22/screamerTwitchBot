import obsws_python as obs

# pass conn info if not in config.toml
cl = obs.ReqClient(host='localhost', port=4455, password='pwtfZfUMYdQbkgzz', timeout=3)

# Toggle the mute state of your Mic input
cl.toggle_input_mute('Mic')
