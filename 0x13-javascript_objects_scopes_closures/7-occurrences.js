#!/usr/bin/node
exports.nbOccurences = function (list, serchElement)
{
    let nOccurences = 0;
    for (let i = 0; i < list.length; i++)
    {
        if (searchElement === list[i])
        {
            nOccurences++;
        }
    }
    return nOccurences;
};