def cigar_party(cigars, is_weekend):
  if is_weekend and cigars > 40:
    return True
  elif not is_weekend and cigars < 40 or cigars > 60:
    return False
  else:
    return True
