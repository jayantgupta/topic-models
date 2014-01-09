stick_breaking_process = function(num_weights, alpha){
#betas = rbeta(num_weights, 1, aplha)
	betas = (1, 2, 4, ncp=0)
	remaining_stick_lengths = c(1, cumprod(1 - betas))[1 : num_weights]
	weights = remaining_stick_lenghts * betas
	weights
}
