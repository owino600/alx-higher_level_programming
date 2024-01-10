#!/usr/bin/node
if (Process.argv[2] === undefined || isNaN(process.argv[2]))
{
    console.log('Missing size');
}
else {
    const x = Number(process.argv[2]);
    let i = 0;
    while (i < x)
    {
        console.log('x'.repeat(x));
        i++;
    }
}