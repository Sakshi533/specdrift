Update from the client: "starvation is STILL happening for the LOWEST tier
-- our bulk jobs sit behind everyone else's mid-tier stuff forever. Fix it
properly." On the follow-up call we pinned down what they mean: in an aging
slot, run the earliest-submitted job from the LOWEST priority tier still
waiting -- not merely any job below the current maximum. Aging slots still
fire at the same positions (4th, 8th, 12th, ...) and still behave like
normal slots when only one priority level remains.
