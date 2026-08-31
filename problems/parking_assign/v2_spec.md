Update: we're letting motorcycles in. A vehicle of size `"XS"` takes a free
S spot if any is free, else a free M, else a free L -- always the smallest
spot size with a free spot, first index within that size. No free spot at
all -> -1, as usual. Cars (`"S"`/`"M"`/`"L"`) are untouched.
