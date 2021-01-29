# Функция проверки файла (на редактирование и создание) перед работой с ним.
"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.
  pass

def WriteFile(AddressFile):  # Check if the file exists:
  """This module is required to read a file (or module).
  It can also check if a file (or module) exists."""
  # Credo: ...
  
  FileOpen = True
  try:  # Открываю файл или Создаю файл:
    File = open(AddressFile, 'w')

    if CheckFile(AddressFile):  # Если файла нет:
      # Я буду проверять на создание файла:
      #TODO Нужно удалить за собой файл AddressFile
      #TODO FileOpen = False  # Нужно сказать что файл не открылся.
      return False  # Файл создать можно.

    else:  # Файл есть:
      # Я буду проверять на редактирование файла:
      try:  # записываю в файл:
        File.write('')
        return False

      except:  # Записать не получилось:
        return None

  except:  # Файл не открылся:
    print("File is not defined. File:", AddressFile)
    FileOpen = False

    return not FileOpen  # True

  finally:
    try:  # Закрываю файл:
      File.close()
      pass

    except:  # Файл не закрылся:
      raise Error
    pass
  pass
