

def generate_trials(subj_code, seed, num_repetitions=25):
    '''
    Writes a file named {subj_code_}trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    seed: an integer specifying the random seed
    num_repetitions: integer specifying total times that combinations of trial type (congruent vs. incongruent) and orientation (upright vs. upside_down) should repeat (total number of trials = 4 * num_repetitions)
    '''
    import os
    import random

    # define general parameters and functions here
    separator = ","
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    trial_types = ["congruent","incongruent"]
    orientations = ["upright","upside_down"]
    num_repetitions = int(num_repetitions)

    def make_incongruent(cur_color): 
        """Return a random color that is different from the color passed in. 
        :Parameters:
            cur_color : string
                Current color of the stimuli
        """
        import random

        #list comprehension solution from assignment code!
        #much better than my original solution, 
        #which is to randomly choosing from the full stimuli list in a while loop and hope for the best...
        incongruent_colors = [stim for stim in colors if stim != cur_color]
        return random.choice(incongruent_colors)

    # create a trials folder if it doesn't already exist
    try:
        os.mkdir('trials')
    except FileExistsError:
        print('Trials directory exists; proceeding to open file')
    f = open(f"trials/{subj_code}_trials.csv","w")

    #write header
    header = separator.join(["subj_code", "seed", "word", 'color','trial_type','orientation'])
    f.write(header+'\n')
    
    # write code to loop through creating and adding trials to the file here
    trials = []
    for cur_trial_type in trial_types: 
        for cur_orientation in orientations: 
            for _ in range(num_repetitions): 
                cur_word = random.choice(colors)
                if cur_trial_type == 'incongruent': 
                    cur_color = make_incongruent(cur_word)
                else: 
                    cur_color = cur_word
                trials.append([subj_code, seed,
                               cur_word, cur_color, 
                               cur_trial_type, cur_orientation])
    random.shuffle(trials)

    for cur_trial in trials:
        #first make all the elements in cur_trial strings, then join them with the separator
        #then write to file
        f.write(separator.join(map(str,cur_trial))+'\n')

    #close the file
    f.close()