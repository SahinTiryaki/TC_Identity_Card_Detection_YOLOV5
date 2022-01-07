import wandb
wandb.login()
api = wandb.Api()

run = api.run("wandb/run-20211214_011140-2zuefx0j/run-2zuefx0j.wandb")
run.file("best.h5").download()