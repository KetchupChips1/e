import colored

colour = lambda txt, clr : colored.stylize(txt, colored.fg(clr))

notes = {}
ntitles = []

print('Welcome to this mini note-taking app!')
print('Type "help" for help\n')


while True:
    ans = input('>')

    ntitles = []
    for i in notes:
        ntitles.append(i)


    if ans.lower() in ('help', 'h'):
        print('help - Shows this message')
        print('note - Creates a note')
        print('read - Reads a note you made by index')
        print('edit - Edits a note you made by index')
        print('list - Shows all of your notes')
        print('delete - Deletes a note by index')
        print('search - Searches for a note by title')
        print('export - Exports one or more notes to a .txt file by index(es)')
        print('quit - Quits the app and loses all of your unexported notes\n')


    elif ans.lower() in ('note', 'n', 'write', 'create'):
        ans = input('\nWhat is your note titled?\n>')
        title = ans if ans.replace(' ', '') != '' else 'Untitled Note'
        ans = input('\nWhat are the contents of your note? Use "^P" ' + \
            'to move to next line.\n>')
        content = ans.replace('^P', '\n')
        ans = input('\nWhat colour do you want your note title to be? ' + \
            'Use hexadecimal colours or leave blank to skip. (e.g., #00ff00)\n>')
        if ans.replace(' ', '') != '':
            try:
                title = colour(title, ans)
            except:
                print(colour('Colour not found, skipping for now.', 'red'))
        notes[title] = content
        print(colour('Note has successfully been taken.\n', 'green'))


    elif ans.lower() in ('read', 'r', 'view'):
        if len(notes) < 1:
            print(colour('No notes have been taken yet.', 'red'))
        else:
            try:
                ans = int(input('\nWhat note do you want to read?\n>'))
                print(f'\n{ans}: {ntitles[ans - 1]}\n{notes[ntitles[ans - 1]]}')
            except Exception as e:
                print(colour(f'An error occured: {e}', 'red'))


    elif ans.lower() in ('edit', 'ed', 'change', 'rewrite'):
        if len(notes) < 1:
            print(colour('No notes have been taken yet.', 'red'))
        else:
            try:
                title = ''
                content = ''
                ans = int(input('\nWhat note do you want to edit?\n>'))
                note = ans
                ans = input('\nWhat is your new title? Leave blank to skip.\n>')
                if ans.replace(' ', '') != '':
                    title = ans
                    ans = input('\nWhat is your title colour? Leave blank to skip.\n>')
                    if ans.replace(' ', '') != '':
                        try:
                            title = colour(title, ans)
                        except:
                            print(colour('Colour not found, skipping for now.', 'red'))
                else:
                    title = ntitles[note - 1]
                ans = input('\nWhat is your note content? Leave blank to skip.\n>')
                if ans.replace(' ', '') != '':
                    content = ans
                else:
                    content = notes[ntitles[note - 1]]
                newnotes = {}
                n = 0
                for i in notes:
                    n += 1
                    if n == note:
                        newnotes[title] = content
                    else:
                        newnotes[ntitles[n - 1]] = notes[ntitles[n - 1]]
                notes = newnotes
                print(colour('Note has successfully been edited.\n', 'green'))
            except Exception as e:
                print(colour(f'An error occured: {e}', 'red'))


    elif ans.lower() in ('list', 'l', 'all'):
        ennotes = enumerate(notes)
        for i, j in ennotes:
            print(f'----------------------------\n{i + 1}: {j}\n{notes[j]}')
        if len(notes) < 1:
            print(colour('No notes have been taken yet.', 'red'))
        else:
            print('')


    elif ans.lower() in ('delete', 'del', 'd', 'remove', 'clear'):
        if len(notes) < 1:
            print(colour('No notes have been taken yet.', 'red'))
        else:
            try:
                ans = int(input('\nWhat note do you want to delete?\n>'))
                conf = input(colour('\nAre you sure? Your note will be deleted forever. ' + \
                        'Type "y" to continue or "n" to cancel.\n', 'yellow'))
                if conf.lower() in ('y', 'yes', 'continue', 'cont'):
                    del notes[ntitles[ans - 1]]
                    print(colour('Note has successfully been deleted.\n', 'green'))
                else:
                    print(colour('Deletion has been cancelled.', 'red'))
            except Exception as e:
                print(colour(f'An error occured: {e}', 'red'))


    elif ans.lower() in ('search', 's', 'find', 'f', 'look'):
        if len(notes) < 1:
            print(colour('No notes have been taken yet.', 'red'))
        else:
            ans = input('\nWhat title do you want to search for?\n>')
            print(f'\nSEARCHING FOR NOTES CONTAINING "{colour(ans, "magenta")}"')
            n = 0
            j = 0
            for i in notes:
                if ans in i:
                    n += 1
                    print(f'----------------------------\n{j + 1}: {i}\n{notes[i]}')
                j += 1
            if n > 0:
                print('')
            else:
                print(colour('No notes have been found.', 'red'))


    elif ans.lower() in ('export', 'ex', 'exp', 'out', 'o', 'save'):
        try:
            ans = input('\nWhat notes do you want to export? ' + \
                'Seperate the notes using commas (e.g., 1, 2, 4, 6) or type "all" for all notes.\n>')
            exnotes = []
            if not ans.lower() in ('all', 'a', 'max', 'every'):
                cont = True
                exnotes += ans.replace(' ', '').replace(',', '')
                for i in range(len(exnotes)):
                    try:
                        exnotes[i] = int(i)
                    except:
                        cont = False
                if cont == True:
                    for i in exnotes:
                        if type(i) == int:
                            if i > len(notes):
                                cont = False
                        else:
                            cont = False
            else:
                cont = True
                for i in range(len(notes)):
                    exnotes.append(i)
            if cont == True:
                ans = input('\nWhat is the file path that you want to export your notes to? ' + \
                    '\nLeave blank to export your notes to the directory which this .py file is currently in. ' + \
                    '\ne.g., C:/Users/you/notes.txt\n>')
                ans = ans.replace('\\', '/')
                if ans.endswith('/'):
                    ans += 'notes.txt'
                if ans.replace(' ', '') == '':
                    ans = 'notes.txt'
                if not ans.endswith('.txt'):
                    ans += '.txt'
                print(colour(f'Exporting to {ans}', 'yellow'))
                write = ''
                for i in exnotes:
                    write += f'\n----------------------------\n{i + 1}: {ntitles[i][9:-4]}\n{notes[ntitles[i]]}'
                file = open(ans, 'w')
                file.write(write)
                file.close()
                print(colour('Successfully exported notes.\n', 'green'))
            else:
                print(colour(f'An error occured; make sure your indexes are integers', 'red'))
        except Exception as e:
            print(colour(f'An error occured: {e}', 'red'))


    elif ans.lower() in ('quit', 'q', 'exit'):
        conf = input(colour('\nAre you sure? All unexported notes will be deleted forever. ' + \
                'Type "y" to continue or "n" to cancel.\n', 'yellow'))
        if conf.lower() in ('y', 'yes', 'continue', 'cont'):
            print(colour('Okay, goodbye!\n', 'green'))
            quit()
        else:
            print(colour('You shall stay here for at least a bit longer.', 'red'))
