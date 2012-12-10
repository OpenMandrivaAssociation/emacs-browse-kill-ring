;; -*- Mode: Emacs-Lisp -*-
; Copyright (C) 2000 by Chmouel Boudjnah
; 
; Redistribution of this file is permitted under the terms of the GNU 
; Public License (GPL)
;

(if (string-match "GNU Emacs" (version))
    (autoload 'browse-kill-ring "emacs-%{rname}" nil t)
  )

(if (string-match "XEmacs" (version))
    (autoload 'browse-kill-ring "xemacs-%{rname}" nil t)
  )
